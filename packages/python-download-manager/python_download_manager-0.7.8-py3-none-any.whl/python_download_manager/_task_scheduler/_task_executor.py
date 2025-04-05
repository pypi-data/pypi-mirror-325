from abc import ABC
from concurrent import futures
from typing import Dict, Union, Iterator

from .._database import CompletedDownloadTask, DownloadTask, DownloadingTask
from .._progress import TqdmProgressManager
from .._structures import ThreadSafeDict
from ._task_downloader import TaskDownloader, ThreadingTaskDownloader
from._done_callbacks import UnregisterProgress

class TaskExecutor(ABC):
    pass


class ThreadingTaskExecutor(TaskExecutor):
    _THREAD_NAME_PREFIX = "DownloadTaskThread"

    def __init__(self, max_workers: int, max_subworkers: int, chunk_size: int):
        self.max_workers = max_workers
        self.max_subworkers = max_subworkers
        self.chunk_size = chunk_size

        self.__futures: Dict[int, futures.Future] = {}
        self.__downloaders: Dict[int, TaskDownloader] = ThreadSafeDict()
        self.__executor = futures.ThreadPoolExecutor(
            self.max_workers, self._THREAD_NAME_PREFIX
        )

    def as_completed(self) -> Iterator[CompletedDownloadTask]:
        for future in futures.as_completed(tuple(self.__futures.values())):
            if future.cancelled():
                continue
            completed_task = future.result()
            if completed_task is None:
                continue
            yield completed_task
        self.__futures.clear()

    def clear(self):
        for future in self.__futures.values():
            future.cancel()
        self.__futures.clear()

        for downloader in self.__downloaders.values():
            downloader.stop()
        # self.__downloaders.clear()

    def cancel_task(self, task_id: int):
        # 如果已经开始执行，则调用相应的downloader的stop方法
        if task_id in self.__downloaders:
            self.__downloaders[task_id].stop()
            self.__futures.pop(task_id)
            return

        # 如果尚未开始执行，则调用cancel方法
        future = self.__futures.pop(task_id)
        future.cancel()

    def shutdown(self):
        self.__executor.shutdown()

    def submit(self, task: Union[DownloadTask, DownloadingTask]):
        # 注册进度条
        TqdmProgressManager.register(task.id, task.file_size)
        future = self.__executor.submit(self._download, task)
        # 任务完成或取消时注销进度条
        # future.add_done_callback(UnregisterProgress(task.id))
        future.add_done_callback(lambda f: TqdmProgressManager.unregister(task.id))
        self.__futures[task.id] = future

    def wait(self) -> list[CompletedDownloadTask]:
        done, _ = futures.wait(tuple(self.__futures.values()))
        completed_tasks = []
        for future in done:
            completed_task = future.result()
            if completed_task is None:
                continue
            completed_tasks.append(completed_task)
        self.__futures.clear()
        return completed_tasks

    def _download(self, task: Union[DownloadTask, DownloadingTask]):
        downloader = ThreadingTaskDownloader(
            task, chunk_size=self.chunk_size, max_workers=self.max_subworkers
        )
        with downloader:
            self.__downloaders[task.id] = downloader
            downloader.start()
            completed_task = downloader.wait_until_complete()
            self.__downloaders.pop(task.id)
        return completed_task
