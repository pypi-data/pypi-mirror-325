import typing as h
from multiprocessing import Process as process_t

from mpss_tools_36.rich_ import progress_t


def NewTrackedTask(
    description: str,
    Task: h.Callable[..., None],
    start: int,
    end_p_1: int,
    progress: progress_t,
    /,
    *,
    t_args: tuple[h.Any, ...] | None = None,
    t_kwargs: dict[str, h.Any] | None = None,
    p_kwargs: dict[str, h.Any] | None = None,
    should_be_started: bool = True,
    **kwargs,
) -> process_t:
    """
    "Minimal" task signature (arguments to appear last if any other):
        (
            progress_or_status: progress_t | status_per_task_h,
            task_id: task_id_t,
            /,
        )
        ->
        None
    """
    if p_kwargs is None:
        p_kwargs = {}
    task_id = progress.NewSubTask(
        description, start_idx=start, end_p_1_idx=end_p_1, **p_kwargs
    )
    p_args = (progress.status_per_task, task_id)

    if t_args is None:
        t_args = ()
    if t_kwargs is None:
        t_kwargs = {}
    output = process_t(target=Task, args=t_args + p_args, kwargs=t_kwargs, **kwargs)

    if should_be_started:
        output.start()

    return output


def NewTrackedSubtasks(
    description: str,
    Task: h.Callable[..., None],
    chunk_bounds: tuple[tuple[int, int], ...],
    progress: progress_t,
    /,
    *,
    t_args: tuple[h.Any, ...] | None = None,
    t_kwargs: dict[str, h.Any] | None = None,
    p_kwargs: dict[str, h.Any] | None = None,
    should_be_started: bool = True,
    **kwargs,
) -> tuple[process_t, ...]:
    """
    description: Base description to be completed with chunk details.
    Task: See NewTrackedTask.
    chunk_bounds: tuple[(start, end_p_1), ...].
    """
    output = []

    descriptions = progress_t.DescriptionsForChunks(description, chunk_bounds)
    for (start, end_p_1), description in zip(chunk_bounds, descriptions, strict=True):
        task = NewTrackedTask(
            description,
            Task,
            start,
            end_p_1,
            progress,
            t_args=t_args,
            t_kwargs=t_kwargs,
            p_kwargs=p_kwargs,
            should_be_started=should_be_started,
            **kwargs,
        )
        output.append(task)

    return tuple(output)


def CloseSubtasks(subtasks: h.Sequence[process_t], /) -> None:
    """"""
    for task in subtasks:
        task.join()
