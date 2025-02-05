import typing as h
from multiprocessing import Process as process_t

from mpss_tools_36.rich_ import progress_t


def NewTrackedProcess(
    description: str,
    Task: h.Callable[..., None],
    n_iterations: int,
    progress: progress_t,
    /,
    *,
    t_args: tuple[h.Any, ...] | None = None,
    t_kwargs: dict[str, h.Any] | None = None,
    p_kwargs: dict[str, h.Any] | None = None,
    start: bool = True,
    **kwargs,
) -> process_t:
    """
    "Minimal" task signature (arguments to appear last if any other):
        (
            progress_or_status: progress_t | status_per_task_h,
            task_id: task_id_t,
            n_iterations: int,
            /,
        )
        ->
        None

    n_iterations: Number of iterations that will be performed by the task.
    """
    if p_kwargs is None:
        p_kwargs = {}
    task_id = progress.NewSubTask(description, total=n_iterations, **p_kwargs)
    p_args = (progress.status_per_task, task_id, n_iterations)

    if t_args is None:
        t_args = ()
    if t_kwargs is None:
        t_kwargs = {}
    output = process_t(target=Task, args=t_args + p_args, kwargs=t_kwargs, **kwargs)

    if start:
        output.start()

    return output
