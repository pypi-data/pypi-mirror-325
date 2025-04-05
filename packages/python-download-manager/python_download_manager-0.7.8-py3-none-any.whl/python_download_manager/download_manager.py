import functools
from concurrent import futures
from pathlib import Path
from typing import Callable, Iterable, Iterator, Optional, Union

from requests import Session

from . import utility
from .database import (
    DatabaseManager,
    Chunk,
    DownloadTask,
    DownloadingTask,
    DeletedDownloadTask,
    CompletedDownloadTask,
    Status,
)
from .decorators import classproperty
from .progress import TqdmProgressManager
from .storage import StorageManager

KB = 1024
MB = 1024 * KB
GB = 1024 * MB
TB = 1024 * GB
PB = 1024 * TB
EB = 1024 * PB
ZB = 1024 * EB
YB = 1024 * ZB


class DownloadManagerMeta(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__class__.instance is not None:
            raise RuntimeError(
                "同一时刻只能存在一个DownloadManager，若要创建新的DownloadManager,请先调用close方法关闭当前的DownloadManager"
            )
        cls.__class__.instance = super(DownloadManagerMeta, cls).__call__(*args, **kwargs)
        return cls.__class__.instance

    def __new__(cls, name, bases, attrs):
        close_method = attrs["close"]

        @functools.wraps(close_method)
        def close_wrapper(*args, **kwargs):
            close_method(*args, **kwargs)
            cls.instance = None

        attrs["close"] = close_wrapper
        return type.__new__(cls, name, bases, attrs)


class DownloadManager(metaclass=DownloadManagerMeta):

    def __init__(
            self,
            database_dir: Union[str, Path] = None,
            max_workers: int = 5,
            max_thread_per_task: int = 5,
            chunk_size: int = 4 * MB,
            headers: dict = None,
            with_progress: bool = True,
    ):
        DatabaseManager.initialize(database_dir)
        # 线程池执行器
        self._thread_pool_executor = futures.ThreadPoolExecutor(max_workers)
        # 每个任务的下载线程数
        self.max_thread_per_task = max_thread_per_task
        # 文件分块的大小
        self.chunk_size = chunk_size
        # 会话
        self._session = Session()
        self._session.headers.update(headers or {})
        # 是否显示进度条
        self.with_progress = with_progress
        # 任务列表
        self._download_task_queue = []
        self._download_task_queue.extend(DatabaseManager.get_all_downloading_task())
        self._download_task_queue.extend(DatabaseManager.get_all_download_task())
        # 已提交的任务列表
        self._submitted_task_list = []
        # 标记为已打开
        self.closed = False

    @classproperty
    def headers(self):
        return self._session.headers

    @classproperty
    def max_workers(self):
        return self._thread_pool_executor._max_workers

    def add_download_task(
            self,
            download_url: str,
            filename: Optional[str] = None,
            save_dir: Union[str, Path] = ".",
            file_size: int = -1,
            callbacks: Iterable[Callable] = tuple(),
    ) -> DownloadTask:
        if filename is None or filename == "":
            filename = utility.get_filename_from_url(download_url)
        download_task = DownloadTask(
            download_url=download_url,
            filename=filename,
            save_dir=save_dir,
            file_size=file_size,
            callbacks=list(callbacks),
        )
        added_download_task = DatabaseManager.add_download_task(download_task)
        self._download_task_queue.append(added_download_task)
        return added_download_task

    def as_completed(self) -> Iterator[CompletedDownloadTask]:
        for completed_task in futures.as_completed(self._submitted_task_list):
            if completed_task.cancelled():
                continue
            yield completed_task.result()
        self._submitted_task_list.clear()

    def close(self):
        if self.closed:
            return
        DatabaseManager.close()
        self._thread_pool_executor.shutdown()
        self._session.close()
        self.closed = True

    def delete_completed_tasks(
            self, task_ids: list[int] = None
    ) -> list[CompletedDownloadTask]:
        """删除已完成的下载任务"""
        return DatabaseManager.delete_completed_tasks(task_ids)

    def delete_deleted_tasks(
            self, task_ids: list[int] = None
    ) -> list[DeletedDownloadTask]:
        """删除在回收站中的任务"""
        return DatabaseManager.delete_deleted_tasks(task_ids)

    def delete_download_tasks(
            self, task_ids: list[int] = None, forever: bool = False
    ) -> list[DownloadTask]:
        """删除等待中的下载任务"""
        # todo 被删除的任务取消下载
        if task_ids is None:
            self._download_task_queue = []
        else:
            self._download_task_queue = [
                task.id not in task_ids for task in self._download_task_queue
            ]
        return DatabaseManager.delete_download_tasks(task_ids, forever)

    def delete_downloading_tasks(
            self, task_ids: list[int] = None, forever: bool = False
    ) -> list[DownloadingTask]:
        """删除下载中的任务"""
        # todo 被删除的任务取消下载并从任务队列中移除
        return DatabaseManager.delete_downloading_tasks(task_ids, forever)

    @staticmethod
    def get_all_download_task() -> list[DownloadTask]:
        """获取所有等待下载的任务"""
        return DatabaseManager.get_all_download_task()

    @staticmethod
    def get_all_downloading_task() -> list[DownloadingTask]:
        """获取所有下载中的任务"""
        return DatabaseManager.get_all_downloading_task()

    @staticmethod
    def get_all_deleted_task() -> list[DeletedDownloadTask]:
        """获取所有已删除的下载任务"""
        return DatabaseManager.get_all_deleted_download_task()

    @staticmethod
    def get_all_completed_task() -> list[CompletedDownloadTask]:
        """获取所有已完成的下载任务"""
        return DatabaseManager.get_all_completed_download_task()

    def start_download(self):
        for task in self._download_task_queue:
            if type(task) is DownloadTask:
                submitted_task = self._thread_pool_executor.submit(
                    self._start_download_task, task
                )
            else:
                submitted_task = self._thread_pool_executor.submit(
                    self._resume_downloading_task, task
                )
            self._submitted_task_list.append(submitted_task)
        self._download_task_queue.clear()

    def wait(self) -> list[CompletedDownloadTask]:
        done, _ = futures.wait(self._submitted_task_list)
        self._submitted_task_list.clear()
        completed_tasks = [future.result() for future in done]
        return completed_tasks

    def _complete_downloading_task(
            self, downloading_task: DownloadingTask
    ) -> CompletedDownloadTask:
        """完成下载任务后的收尾工作"""
        # 注销进度条
        if self.with_progress:
            TqdmProgressManager.unregister(downloading_task.id)
        # 在存储管理器中关闭文件
        StorageManager.close(
            downloading_task.file_path, downloading_task.last_modified_time
        )
        # 下载完成后执行回调任务
        for callback in downloading_task.callbacks:
            callback()
        # 下载完成后记录到数据库
        return DatabaseManager.complete_download_task(downloading_task)

    def _download_chunk(self, chunk: Chunk, downloading_task: DownloadingTask):
        # 将文件块的状态更新为“下载中”
        chunk.status = Status.DOWNLOADING.value
        DatabaseManager.update_chunk(chunk)
        # 配置请求头
        headers = downloading_task.headers.copy()
        headers.update(chunk.headers)
        # 下载并写入磁盘
        with self._session.get(
                downloading_task.download_url, headers=headers
        ) as response:
            content = response.content
            StorageManager.write(downloading_task.file_path, content, chunk.start)
        # 更新进度条
        if self.with_progress:
            TqdmProgressManager.update(downloading_task.id, chunk.size)
        # 下载完成后将文件块的状态更新为“已完成”
        chunk.status = Status.FINISHED.value
        DatabaseManager.update_chunk(chunk)

    def _download_chunks_with_multi_thread(
            self, downloading_task: DownloadingTask, chunks: list[Chunk]
    ):
        """使用多线程下载文件块"""
        # 注册进度条，并恢复进度
        if self.with_progress:
            downloaded_size = 0
            for chunk in chunks:
                if chunk.status == Status.FINISHED.value:
                    downloaded_size += chunk.size
            info = {"task_id": downloading_task.id}
            TqdmProgressManager.register(
                downloading_task.id, total=downloading_task.file_size, info=info
            )
            TqdmProgressManager.update(downloading_task.id, downloaded_size)
        # 启用多线程下载各个文件块
        with futures.ThreadPoolExecutor(
                max_workers=self.max_thread_per_task
        ) as executor:
            submitted_tasks = [
                executor.submit(self._download_chunk, chunk, downloading_task)
                for chunk in chunks
                if chunk.status != Status.FINISHED.value
            ]
            futures.wait(submitted_tasks)

    def _download_simply(self, downloading_task: DownloadTask):
        """使用单线程下载文件
        通常用于不支持断点续传的任务，以及文件大小小于文件块大小的情况
        """
        # 初始化定制请求头
        headers = {}
        headers.update(downloading_task.headers)
        # 注册进度条
        TqdmProgressManager.register(
            downloading_task.id,
            total=downloading_task.file_size,
            info={"task_id": downloading_task.id},
        )
        # 开始下载
        with self._session.get(
                downloading_task.download_url, headers=headers, stream=True
        ) as response:
            index = 0
            for content in response.iter_content(64 * MB):
                StorageManager.write(downloading_task.file_path, content, index)
                index += len(content)
                # 更新进度条
                if self.with_progress:
                    TqdmProgressManager.update(downloading_task.id, len(content))

    def _resume_downloading_task(
            self, downloading_task: DownloadingTask
    ) -> CompletedDownloadTask:
        """恢复下载任务"""
        # 在存储管理器中打开文件，等待写入
        StorageManager.open(
            file_path=downloading_task.file_path,
            file_size=downloading_task.file_size,
            file_writer_class_name=downloading_task.file_writer_class_name,
        )
        # 查出所有文件块
        chunks = DatabaseManager.get_all_downloading_task_chunks(downloading_task)
        # 恢复下载
        if len(chunks) > 1:
            self._download_chunks_with_multi_thread(downloading_task, chunks)
        else:
            self._download_simply(downloading_task)
        # 下载完成后执行收尾工作
        return self._complete_downloading_task(downloading_task)

    def _start_download_task(
            self, download_task: DownloadTask
    ) -> CompletedDownloadTask:
        """启动下载任务"""
        # 发送head请求，确定要下载的文件的大小及修改时间等元数据
        if not download_task.response_headers:
            with self._session.head(
                    download_task.download_url, headers=download_task.headers
            ) as response:
                download_task.response_headers = response.headers
                content_length = response.headers.get("Content-Length")
            if content_length is not None:
                download_task.file_size = int(content_length)
        # 在存储管理器中打开文件，等待写入
        file_writer_class_name = StorageManager.open(
            file_path=download_task.file_path, file_size=download_task.file_size
        )
        download_task.file_writer_class_name = file_writer_class_name
        # 将信息记录到数据库
        DatabaseManager.update_download_task(download_task)
        # 根据文件大小及块大小分割出文件块
        chunks = utility.slice_file(download_task.file_size, self.chunk_size)
        # 将下载任务标记为下载中
        downloading_task, added_chunks = DatabaseManager.start_download_task(
            download_task, chunks
        )

        # 如果文件块数大于1，则使用多线程下载器
        if len(added_chunks) > 1:
            self._download_chunks_with_multi_thread(downloading_task, added_chunks)
        else:
            self._download_simply(download_task)
        # 执行下载完成后的收尾工作
        return self._complete_downloading_task(downloading_task)

    def __enter__(self):
        return self

    def __exit__(self, error_type, error_value, traceback):
        self.close()
        return False
