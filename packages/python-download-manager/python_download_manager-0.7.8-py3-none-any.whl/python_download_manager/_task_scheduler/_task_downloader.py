from abc import ABC, abstractmethod
from concurrent import futures
import logging
from pathlib import Path
import threading
import time
from typing import Union

from .._database import (
    DatabaseManager,
    Chunk,
    CompletedDownloadTask,
    DownloadTask,
    DownloadingTask,
    Status,
)
from .._session_manager import SessionManager
from .._storage import StorageManager
from .. import _utility
from .._consts import MB, NOFILENAME
from .._progress import TqdmProgressManager

# logger
_logger = logging.getLogger("TaskDownloader")
_log_dir = Path(".pdm/logs")
_log_dir.mkdir(parents=True, exist_ok=True)
_error_hangler = logging.FileHandler(
    _log_dir.joinpath("error_tasks.log"), encoding="utf-8"
)
_error_hangler.setLevel(logging.ERROR)
_logger.addHandler(_error_hangler)


class TaskDownloader(ABC):

    @abstractmethod
    def close(self): ...

    @abstractmethod
    def start(self): ...

    @abstractmethod
    def stop(self): ...

    @abstractmethod
    def wait_until_complete(self) -> CompletedDownloadTask: ...

    def __enter__(self):
        return self

    def __exit__(self, error_type, error_value, traceback):
        self.close()
        return False


class ThreadingTaskDownloader(TaskDownloader):
    _THREAD_NAME_PREFIX = "DownloadChunkThread"

    def __init__(
        self,
        task: Union[DownloadTask, DownloadingTask],
        chunk_size: int,
        max_workers: int,
    ):
        self.max_workers = max_workers
        self.chunk_size = chunk_size

        # 初始化下载任务
        self.task, self.chunks = self.__init_task(task)

        self.__stop_event = threading.Event()
        self.__futures = []
        # 打开文件等待写入
        StorageManager.open(
            self.task.file_path, self.task.file_size, self.task.file_writer_class_name
        )
        # 更新进度条信息
        downloaded_size = 0
        for chunk in self.chunks:
            downloaded_size += chunk.downloaded_size
        info = {"filename": self.task.filename}
        TqdmProgressManager.set_total(self.task.id, self.task.file_size)
        TqdmProgressManager.set_progress(self.task.id, downloaded_size)
        TqdmProgressManager.set_info(self.task.id, info)

    def __init_task(self, task: DownloadTask) -> (DownloadingTask, list[Chunk]):
        """初始化下载任务"""
        if type(task) is DownloadingTask:
            chunks = DatabaseManager.get_all_downloading_task_chunks(task)
            return task, chunks

        # 发送head请求，确认文件大小和文件名等信息
        if not task.response_headers or task.filename == NOFILENAME:
            with SessionManager.head(
                task.download_url, headers=task.headers, proxies=task.proxies
            ) as response:
                # 检查response的状态码
                if response.status_code != 200:
                    _logger.error(
                        f"head请求失败:{task.download_url},状态码:{response.status_code}"
                    )
                    self.stop()
                    return
                # 文件大小
                task.response_headers = response.headers
                # 文件名
                if task.filename == NOFILENAME:
                    task.filename = response.headers.get(
                        "Content-Disposition",
                        _utility.get_filename_from_url(response.url),
                    )

            # 更新下载任务信息
            DatabaseManager.update_download_task(task)

        # 根据文件大小及块大小分割出文件块
        chunks = _utility.slice_file(task.file_size, self.chunk_size)
        # 将下载任务标记为下载中
        downloading_task, added_chunks = DatabaseManager.start_download_task(
            task, chunks
        )
        return downloading_task, added_chunks

    def close(self):
        # 在存储管理器中关闭文件
        StorageManager.close(self.task.file_path, self.task.last_modified_time)

    def start(self):
        # 提交文件块下载任务
        with futures.ThreadPoolExecutor(
            max_workers=min(self.max_workers, len(self.chunks)),
            thread_name_prefix=self._THREAD_NAME_PREFIX,
        ) as executor:
            self.__futures = [
                executor.submit(self.__download_chunk, chunk)
                for chunk in self.chunks
                if chunk.status != Status.FINISHED.value
            ]

    def stop(self):
        for future in self.__futures:
            future.cancel()
        self.__futures.clear()
        self.__stop_event.set()
        StorageManager.stop(self.task.file_path)

    def wait_until_complete(self) -> CompletedDownloadTask:
        # 等待所有文件块下载完成
        futures.wait(tuple(self.__futures))
        # 检查是否全部文件块都已经下载完成
        for chunk in self.chunks:
            if chunk.status != Status.FINISHED.value:
                return
        # 执行下载完成后的回调函数
        for callback in self.task.callbacks:
            callback(self.task)
        # 记录到数据库
        return DatabaseManager.complete_download_task(self.task)

    def __download_chunk(self, chunk: Chunk):
        # 将文件块的状态更新为“下载中”
        chunk.status = Status.DOWNLOADING.value
        DatabaseManager.update_chunk(chunk)
        # 配置请求头
        headers = self.task.headers.copy()
        if self.task.file_size > 0:
            headers.update(chunk.range_headers)
        # 发送请求下载文件
        with SessionManager.get(
            self.task.download_url,
            headers=headers,
            proxies=self.task.proxies,
            stream=True,
        ) as response:
            if response.status_code not in (200, 206):
                # 将文件块的状态改为"error"
                chunk.status = Status.ERROR.value
                DatabaseManager.update_chunk(chunk)
                # 写入日志
                _logger.error(
                    f"文件块请求失败:{self.task.download_url},状态码:{response.status_code},start={chunk.start},end={chunk.end}"
                )
                # 停止
                self.stop()
                return
            for content in response.iter_content(4 * MB):
                if self.__stop_event.is_set():
                    return
                # 写入磁盘
                written_size = StorageManager.write(
                    self.task.file_path, content, chunk.start + chunk.downloaded_size
                )
                # 更新文件块信息
                chunk.downloaded_size += written_size
                DatabaseManager.update_chunk(chunk)
                # 更新进度条
                TqdmProgressManager.update(self.task.id, written_size)

        # 下载完成后将文件块的状态更新为“已完成”
        chunk.status = Status.FINISHED.value
        DatabaseManager.update_chunk(chunk)


class AsyncTaskDownloader(TaskDownloader):
    pass
