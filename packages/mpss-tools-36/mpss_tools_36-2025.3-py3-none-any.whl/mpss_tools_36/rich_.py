import typing as h
from multiprocessing import Manager as NewSharingManager
from multiprocessing.managers import DictProxy as shared_dict_t
from multiprocessing.managers import SyncManager as sharing_manager_t

from rich.progress import Progress as base_t
from rich.progress import Task as task_t
from rich.progress import TaskID as task_id_t
from rich.progress import TimeRemainingColumn as column_eta_t

status_per_task_h = shared_dict_t[task_id_t, int | float]


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

    @property
    def n_iterations(self) -> int:
        """
        Number of iterations that will be performed by the (unique) task.

        Only for unique task/sequential tasks.
        """
        n_iterations = self.unique_task.total
        if (n_iterations is None) or not n_iterations.is_integer():
            raise TypeError

        return int(n_iterations)

    @classmethod
    def New(
        cls,
        *columns,
        refresh_per_second: int | float = 1.0,
        speed_estimate_period: int | float = 10.0,
        elapsed_when_finished: bool = True,
        with_task: tuple[str, int | float] | tuple[str, dict[str, h.Any]] | None = None,
        for_several_processes: bool = False,
        with_overall_progress: str | None = "Overall",
        start: bool = True,
        **kwargs,
    ) -> h.Self:
        """
        with_task, if not None:
        - description, total
        - description, kwargs

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
        elif with_task is not None:
            description, total_or_kwargs = with_task
            if isinstance(total_or_kwargs, int | float):
                total_or_kwargs = {"total": total_or_kwargs}
            task_id = output.add_task(description, **total_or_kwargs)
            output.unique_task = output.tasks[task_id]

        if start:
            output.start()

        return output

    def NewTask(self, description: str, /, **kwargs) -> task_id_t:
        """
        For both unique task/sequential tasks and parallel tasks.
        """
        output = self.add_task(description, **kwargs)

        if self.status_per_task is not None:
            self.status_per_task[output] = 0.0
            if self.global_task is not None:
                self.global_task.total += self.tasks[output].total

        return output

    NewSubTask = NewTask

    def Iterator(self, *, zero_based: bool = True) -> h.Iterator[int]:
        """
        Only for unique task/sequential tasks.
        """
        n_iterations = self.unique_task.total
        if (n_iterations is None) or not n_iterations.is_integer():
            raise TypeError

        n_iterations = int(n_iterations)
        if zero_based:
            indices = range(n_iterations)
        else:
            indices = range(1, n_iterations + 1)

        task_id = self.unique_task.id
        for idx in indices:
            self.update(task_id, completed=idx)
            yield idx

    def CloseIterator(self) -> None:
        """
        Only for unique task/sequential tasks.
        """
        self.update(self.unique_task.id, completed=self.unique_task.total)
        self.stop()

    @staticmethod
    def Update(
        progress_or_status: base_t | status_per_task_h,
        task_id: task_id_t,
        completed: int | float,
        /,
    ) -> None:
        """
        For both unique task/sequential tasks and parallel tasks.
        """
        if isinstance(progress_or_status, base_t):
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
                # task_id cannot be global_task.id.
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
