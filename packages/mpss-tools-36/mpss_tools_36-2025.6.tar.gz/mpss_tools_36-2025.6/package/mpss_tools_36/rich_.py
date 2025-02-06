import typing as h
from multiprocessing import Manager as NewSharingManager
from multiprocessing.managers import DictProxy as shared_dict_t
from multiprocessing.managers import SyncManager as sharing_manager_t

from rich.progress import Progress as base_t
from rich.progress import Task as task_t
from rich.progress import TaskID as task_id_t
from rich.progress import TimeRemainingColumn as column_eta_t

status_per_task_h = (
    dict[task_id_t | tuple[task_id_t, str], int | float]
    | shared_dict_t[task_id_t | tuple[task_id_t, str], int | float]
)


class progress_t(base_t):
    """
    Incompatible with the dataclass extension.
    """

    unique_task: task_t | None = None
    #
    global_task: task_t | None = None
    status_per_task: status_per_task_h | None = None
    sharing_manager: sharing_manager_t | None = None

    @property
    def task_id(self) -> task_id_t:
        """
        Only for unique task/sequential tasks.
        """
        return self.unique_task.id

    @classmethod
    def New(
        cls,
        *columns,
        refresh_per_second: int | float = 1.0,
        speed_estimate_period: int | float = 10.0,
        elapsed_when_finished: bool = True,
        with_task: (
            tuple[str, int | float]
            | tuple[str, int | float, dict[str, h.Any]]
            | tuple[str, int | float, int | float]
            | tuple[str, int | float, int | float, dict[str, h.Any]]
            | None
        ) = None,
        for_several_processes: bool = False,
        with_overall_progress: str | None = "Overall",
        should_be_started: bool = True,
        **kwargs,
    ) -> h.Self:
        """
        For unique task/sequential tasks, with_task must be either one of:
        - (description: str, n_iterations: int | float)
        - (description: str, n_iterations: int | float, kwargs: dict[str, h.Any])
        - (description: str, start: int | float, end_p_1: int | float)
        - (description: str, start: int | float, end_p_1: int | float, kwargs: dict[str, h.Any])

        For both unique task/sequential tasks and parallel tasks, but only for unique
        task/sequential tasks if with_task is not None.
        """
        if columns.__len__() == 0:
            columns = base_t.get_default_columns()
            if elapsed_when_finished:
                columns = columns[:-1] + (column_eta_t(elapsed_when_finished=True),)

        output = cls(
            *columns,
            refresh_per_second=refresh_per_second,
            speed_estimate_period=speed_estimate_period,
            **kwargs,
        )

        if for_several_processes:
            output.sharing_manager = NewSharingManager()
            output.status_per_task = output.sharing_manager.dict()
            if with_overall_progress is not None:
                task_id = output.add_task(with_overall_progress.upper(), total=0.0)
                output.global_task = output.tasks[task_id]
        else:
            output.status_per_task = {}
            if with_task is not None:
                description, start_or_n_iterations, *rest = with_task
                if (length := rest.__len__()) == 0:
                    start_idx, end_p_1_idx = 0, None
                    n_iterations = start_or_n_iterations
                    kwargs = {}
                else:
                    # assert isinstance(rest[0], int| float)
                    start_idx = start_or_n_iterations
                    end_p_1_idx = rest[0]
                    n_iterations = None
                    if length == 1:
                        kwargs = {}
                    else:
                        assert length == 2
                        kwargs = rest[1]

                task_id = output.NewTask(
                    description,
                    start_idx=start_idx,
                    end_p_1_idx=end_p_1_idx,
                    n_iterations=n_iterations,
                    **kwargs,
                )
                output.unique_task = output.tasks[task_id]

        if should_be_started:
            output.start()

        return output

    def NewTask(
        self,
        description: str,
        /,
        start_idx: int = 0,
        end_p_1_idx: int | None = None,
        n_iterations: int | None = None,
        **kwargs,
    ) -> task_id_t:
        """
        For both unique task/sequential tasks and parallel tasks.
        """
        if end_p_1_idx is None:
            end_p_1_idx = start_idx + n_iterations
        else:
            n_iterations = end_p_1_idx - start_idx

        kwargs["total"] = n_iterations
        output = self.add_task(description, **kwargs)

        self.status_per_task[(output, "start")] = start_idx
        self.status_per_task[(output, "end_p_1")] = end_p_1_idx
        self.status_per_task[output] = 0.0

        if self.global_task is not None:
            self.global_task.total += self.tasks[output].total

        return output

    NewSubTask = NewTask

    @staticmethod
    def TaskRange(
        progress_or_status: base_t | status_per_task_h,
        task_id: task_id_t,
        /,
        *,
        mode: h.Literal["0", "1", "r"] = "r",
    ) -> range:
        """
        For both unique task/sequential tasks and parallel tasks.
        """
        if isinstance(progress_or_status, progress_t):
            status_per_task = progress_or_status.status_per_task
        else:
            status_per_task = progress_or_status
        start = status_per_task[(task_id, "start")]
        end_p_1 = status_per_task[(task_id, "end_p_1")]

        if mode == "r":
            return range(start, end_p_1)

        if mode == "0":
            return range(end_p_1 - start)

        assert mode == "1"
        return range(1, end_p_1 - start + 1)

    @staticmethod
    def Update(
        progress_or_status: base_t | status_per_task_h,
        task_id: task_id_t,
        /,
        *,
        i0: int | float | None = None,
        i1: int | float | None = None,
        ir: int | float | None = None,
    ) -> None:
        """
        i0: zero-based index
        i1: one-based index
        ir: range-based index

        For both unique task/sequential tasks and parallel tasks.
        """
        is_a_progress = isinstance(progress_or_status, progress_t)

        if i0 is not None:
            completed = i0 + 1
        elif i1 is not None:
            completed = i1
        else:
            key = (task_id, "start")
            if is_a_progress:
                start = progress_or_status.status_per_task[key]
            else:
                start = progress_or_status[key]
            completed = ir - start + 1

        if is_a_progress:
            progress_or_status.update(task_id, completed=completed)
        else:
            progress_or_status[task_id] = completed

    def TrackUpdates(self, *, should_close_progress: bool = True) -> None:
        """
        Only for parallel tasks.
        """
        global_task = self.global_task
        status_per_task = self.status_per_task

        while not self.finished:
            completed_global = 0.0
            for task_id, completed in status_per_task.items():
                if not isinstance(task_id, tuple):
                    # Note: task_id cannot be global_task.id.
                    self.update(task_id, completed=completed)
                    completed_global += completed

            if global_task is not None:
                # min: For round-off errors.
                completed_global = min(completed_global, global_task.total)
                self.update(global_task.id, completed=completed_global)

        if should_close_progress:
            self.stop()

    def PrintAbove(self, *args, **kwargs) -> None:
        """"""
        self.console.print(*args, **kwargs)

    Close = base_t.stop

    def __del__(self) -> None:
        """"""
        self.stop()

        if self.sharing_manager is not None:
            self.sharing_manager.shutdown()

        if (Delete := getattr(base_t, "__del__", None)) is not None:
            Delete(self)
