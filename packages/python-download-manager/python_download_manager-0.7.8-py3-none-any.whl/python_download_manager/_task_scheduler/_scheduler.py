"""
功能：
    1. 实现多线程管理，线程对应一个任务，线程内再开若干个子线程来下载文件块
    2. 用线程事件来实现下载任务的中止
"""

from abc import ABC, abstractmethod
from collections import deque
from concurrent import futures
from typing import Union, Dict, Iterator

from .._consts import MB
from .._database import (
    DatabaseManager,
    DownloadTask,
    DownloadingTask,
    CompletedDownloadTask,
)
from .._progress import TqdmProgressManager
from .._session_manager import SessionManager
from .._structures import ThreadSafeDict
from ._task_executor import TaskExecutor, ThreadingTaskExecutor
from ._done_callbacks import UnregisterProgress


class TaskScheduler(ABC):
    _unsubmitted_tasks: deque[Union[DownloadTask, DownloadingTask]]
    _submitted_tasks: Dict[int, futures.Future]


class ThreadingTaskScheduler(TaskScheduler):
    _THREAD_NAME_PREFIX = "DownloadTaskThread"

    def __init__(
        self,
        max_workers: int,
        max_subworkers: int,
        chunk_size: int,
    ):
        self.max_workers = max_workers
        self.max_subworkers = max_subworkers
        self.chunk_size = chunk_size

        self._unsubmitted_tasks: deque[Union[DownloadTask, DownloadingTask]] = deque()
        self._submitted_tasks: Dict[int, Union[DownloadTask, DownloadingTask]] = {}

        self._executor = ThreadingTaskExecutor(max_workers, max_subworkers, chunk_size)

    def add_task(self, task: Union[DownloadTask, DownloadingTask]):
        """添加任务"""
        self._unsubmitted_tasks.append(task)

    def as_completed(self) -> Iterator[CompletedDownloadTask]:
        # 将下载完成的任务移除
        for completed_task in self._executor.as_completed():
            self._submitted_tasks.pop(completed_task.id)
            yield completed_task
        
        # 将未下载完成的任务重新入队
        uncompleted_task_ids = [task.id for task in self._submitted_tasks.values()]
        self._unsubmitted_tasks.extend(DatabaseManager.get_all_downloading_task(uncompleted_task_ids))
        self._unsubmitted_tasks.extend(DatabaseManager.get_all_download_task(uncompleted_task_ids))
        
        self._submitted_tasks.clear()

    def close(self):
        self._executor.shutdown()

    def start(self):
        for task in self._unsubmitted_tasks:
            # 提交任务
            self._executor.submit(task)
            self._submitted_tasks[task.id] = task
        self._unsubmitted_tasks.clear()

    def delete_task(self, task_id: int):
        # 如果尚未提交，则直接移除出队列
        for task in self._unsubmitted_tasks:
            if task.id == task_id:
                self._unsubmitted_tasks.remove(task)
                return

        # 如果已经提交
        self._submitted_tasks.pop(task_id)
        self._executor.cancel_task(task_id)

    def delete_tasks(self, task_ids: list[int] = None):
        # 如果参数为空，则清空所有任务
        if task_ids is None:
            self._unsubmitted_tasks.clear()
            self._submitted_tasks.clear()
            self._executor.clear()
            return

        # 移除尚未提交的任务
        self._unsubmitted_tasks = deque(
            task for task in self._unsubmitted_tasks if task.id not in task_ids
        )
        # 取消并移除已提交的任务
        for task_id in task_ids:
            if task_id not in self._submitted_tasks:
                continue
            self._submitted_tasks.pop(task_id)
            self._executor.cancel_task(task_id)

    def stop_task(self, task_id: int):
        if task_id not in self._submitted_tasks:
            return
        # 取消执行
        self._executor.cancel_task(task_id)
        
        # 将取消的任务加入等待队列
        task = self._submitted_tasks.pop(task_id)
        self._unsubmitted_tasks.extendleft(DatabaseManager.get_all_download_task([task.id]))
        self._unsubmitted_tasks.extendleft(DatabaseManager.get_all_downloading_task([task.id]))

    def stop_tasks(self, task_ids: list[int] = None):
        # 如果参数为空，则直接停止运行，取消所有任务
        if task_ids is None:
            self.stop()
            return

        for task_id in task_ids:
            self.stop_task(task_id)

    def stop(self):
        """停止运行"""
        # 取消所有已提交的任务
        self._executor.clear()
        
        # 让已提交的任务重新入队
        uncompleted_task_ids = [task.id for task in self._submitted_tasks.values()]
        self._unsubmitted_tasks.extend(DatabaseManager.get_all_downloading_task(uncompleted_task_ids))
        self._unsubmitted_tasks.extend(DatabaseManager.get_all_download_task(uncompleted_task_ids))
        
        self._submitted_tasks.clear()

    def wait(self) -> list[CompletedDownloadTask]:
        completed_tasks = self._executor.wait()

        # 移除下载完成的任务
        for completed_task in completed_tasks:
            self._submitted_tasks.pop(completed_task.id)

        # 将未下载完成的任务重新入队
        uncompleted_task_ids = [task.id for task in self._submitted_tasks.values()]
        self._unsubmitted_tasks.extend(DatabaseManager.get_all_downloading_task(uncompleted_task_ids))
        self._unsubmitted_tasks.extend(DatabaseManager.get_all_download_task(uncompleted_task_ids))

        self._submitted_tasks.clear()

        return completed_tasks


class ProcessingTaskScheduler(TaskScheduler):

    def __init__(self, max_workers: int = None, max_subworkers: int = None):
        self._executor = futures.ProcessPoolExecutor(max_workers=max_workers)
