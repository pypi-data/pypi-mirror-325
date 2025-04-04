from collections import deque
import functools
import logging
from concurrent import futures
from pathlib import Path
import re
from typing import Callable, Iterable, Iterator, Optional, Union

from requests import Session
from requests.structures import CaseInsensitiveDict

from . import _utility
from ._consts import MB, NOFILENAME
from ._database import (
    DatabaseManager,
    Chunk,
    DownloadTask,
    DownloadingTask,
    DeletedDownloadTask,
    CompletedDownloadTask,
    Status,
)
from ._progress import TqdmProgressManager
from ._storage import StorageManager
from ._session_manager import SessionManager
from ._task_scheduler import ThreadingTaskScheduler
from ._typehint import StrPath


class DownloadManagerMeta(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__class__.instance is not None:
            raise RuntimeError(
                "同一时刻只能存在一个DownloadManager，若要创建新的DownloadManager,请先调用close方法关闭当前的DownloadManager"
            )
        cls.__class__.instance = super(DownloadManagerMeta, cls).__call__(
            *args, **kwargs
        )
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
        database_dir: StrPath = None,
        max_workers: int = 5,
        max_thread_per_task: int = 5,
        chunk_size: int = 4 * MB,
        headers: dict = None,
        proxies: dict = None,
        with_progress: bool = True,
    ):
        # 初始化数据库
        DatabaseManager.initialize(database_dir)
        # 任务调度器
        self._task_scheduler = ThreadingTaskScheduler(
            max_workers, max_thread_per_task, chunk_size
        )
        # 初始化会话管理器
        self.headers = headers
        self.proxies = proxies
        SessionManager.initialize(headers, proxies)
        # 初始化进度条管理器
        if with_progress:
            TqdmProgressManager.initialize()
        # 标记为已打开
        self.closed = False

    @property
    def max_workers(self):
        return self._task_scheduler.max_workers

    def add_download_task(
        self,
        download_url: str,
        *,
        filename: Optional[str] = None,
        save_dir: StrPath = ".",
        callbacks: Iterable[Callable] = tuple(),
        headers: dict = None,
        proxies: dict = None,
        response_headers: dict = None,
    ) -> DownloadTask:
        # 如果response_headers不为空，并且文件名没指定的话
        # 则检查一下response_headers里面是否包含有文件名
        if response_headers and not filename:
            response_headers = CaseInsensitiveDict(response_headers)
            value = response_headers.get("Content-Disposition", "")
            match = re.search(r'filename="(.+)"', value)
            if match:
                filename = match.group(1)
        # 将下载任务添加到数据库中
        download_task = DownloadTask(
            download_url=download_url,
            filename=filename or NOFILENAME,
            save_dir=save_dir,
            callbacks=list(callbacks),
            headers=headers or {},
            proxies=proxies or {},
            response_headers=response_headers or {},
        )
        added_download_task = DatabaseManager.add_download_task(download_task)
        self._task_scheduler.add_task(added_download_task)
        return added_download_task

    def as_completed(self) -> Iterator[CompletedDownloadTask]:
        return self._task_scheduler.as_completed()

    def close(self):
        if self.closed:
            return
        DatabaseManager.close()
        self._task_scheduler.close()
        SessionManager.close()
        TqdmProgressManager.close()
        self.closed = True

    def delete_completed_tasks(
        self, task_ids: list[int] = None, *, with_file: bool = False
    ) -> list[CompletedDownloadTask]:
        """删除已完成的下载任务"""
        deleted_tasks = DatabaseManager.delete_completed_tasks(task_ids)

        if with_file:
            for deleted_task in deleted_tasks:
                StorageManager.delete(deleted_task.file_path)

        return deleted_tasks

    def delete_deleted_tasks(
        self, task_ids: list[int] = None, *, with_file: bool = False
    ) -> list[DeletedDownloadTask]:
        """删除在回收站中的任务"""
        deleted_tasks = DatabaseManager.delete_deleted_tasks(task_ids)

        if with_file:
            for deleted_task in deleted_tasks:
                StorageManager.delete(deleted_task.file_path)

        return deleted_tasks

    def delete_download_tasks(
        self, task_ids: list[int] = None, *, forever: bool = False
    ) -> list[DownloadTask]:
        """删除等待中的下载任务"""
        self._task_scheduler.delete_tasks(task_ids)
        return DatabaseManager.delete_download_tasks(task_ids, forever)

    def delete_downloading_tasks(
        self,
        task_ids: list[int] = None,
        *,
        forever: bool = False,
        with_file: bool = False,
    ) -> list[DownloadingTask]:
        """删除下载中的任务"""
        self._task_scheduler.delete_tasks(task_ids)
        deleted_tasks = DatabaseManager.delete_downloading_tasks(task_ids, forever)

        if with_file:
            for deleted_task in deleted_tasks:
                StorageManager.delete(deleted_task.file_path)

        return deleted_tasks

    @staticmethod
    def get_all_download_task(task_ids: list[int] = None) -> list[DownloadTask]:
        """获取所有等待下载的任务"""
        return DatabaseManager.get_all_download_task(task_ids)

    @staticmethod
    def get_all_downloading_task(task_ids: list[int] = None) -> list[DownloadingTask]:
        """获取所有下载中的任务"""
        return DatabaseManager.get_all_downloading_task(task_ids)

    @staticmethod
    def get_all_deleted_task(task_ids: list[int] = None) -> list[DeletedDownloadTask]:
        """获取所有已删除的下载任务"""
        return DatabaseManager.get_all_deleted_download_task(task_ids)

    @staticmethod
    def get_all_completed_task(
        task_ids: list[int] = None,
    ) -> list[CompletedDownloadTask]:
        """获取所有已完成的下载任务"""
        return DatabaseManager.get_all_completed_download_task(task_ids)

    def start(self):
        self._task_scheduler.start()

    def stop(self):
        self._task_scheduler.stop()

    def wait(self) -> list[CompletedDownloadTask]:
        return self._task_scheduler.wait()

    def __enter__(self):
        return self

    def __exit__(self, error_type, error_value, traceback):
        self.close()
        return False
