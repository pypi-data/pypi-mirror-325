from abc import ABC, abstractmethod
from collections import deque, OrderedDict
from dataclasses import dataclass, field
from threading import Lock
from typing import Hashable, Type

from ._adapter import ProgressAdapter, TqdmAdapter
from .._decorators import synchronized

_progress_lock = Lock()


@dataclass
class RegisteredTask:
    key: Hashable
    total: int
    progress: int = 0
    info: dict = field(default_factory=dict)


class ProgressManager(ABC):

    @classmethod
    @abstractmethod
    def register(
        cls, key: Hashable, total: int, *, progress: int = 0, info: dict = None
    ) -> ProgressAdapter: ...

    @classmethod
    @abstractmethod
    def unregister(cls, key: Hashable) -> ProgressAdapter: ...

    @classmethod
    @abstractmethod
    def update(cls, key: Hashable, increment: int):
        ...

    @classmethod
    @abstractmethod
    def set_total(cls, key: Hashable, total: int):
        ...

    @classmethod
    @abstractmethod
    def set_progress(cls, key: Hashable, progress):
        ...


class TqdmProgressManager(ProgressManager):
    _global_progress_bar: ProgressAdapter = None
    _progress_bars: OrderedDict[Hashable, TqdmAdapter] = {}
    _progress_bar_pool: deque[TqdmAdapter] = deque()
    _registered_tasks: dict[Hashable, RegisteredTask] = {}

    @classmethod
    def initialize(cls):
        cls._global_progress_bar = TqdmAdapter(0, desc="Global")

    @classmethod
    @synchronized(_progress_lock)
    def close(cls):
        if cls._global_progress_bar is None:
            return

        cls._global_progress_bar.close()
        for bar in cls._progress_bars.values():
            bar.close()
        cls._progress_bars.clear()
        for bar in cls._progress_bar_pool:
            bar.close()
        cls._progress_bar_pool.clear()
        cls._registered_tasks.clear()

    @classmethod
    @synchronized(_progress_lock)
    def register(
        cls, key: Hashable, total: int, *, progress: int = 0, info: dict = None
    ):
        if cls._global_progress_bar is None:
            return
        # 注册信息
        registered_task = RegisteredTask(key, total, progress, info or {})
        cls._registered_tasks[key] = registered_task
        # 更新总进度条
        cls._global_progress_bar.total += total
        cls._global_progress_bar.progress += progress
        cls._global_progress_bar.info = {"rest": len(cls._registered_tasks)}

    @classmethod
    @synchronized(_progress_lock)
    def unregister(cls, key: Hashable):
        if cls._global_progress_bar is None:
            return
        # 碰到未注册的任务信息时报错
        if key not in cls._registered_tasks:
            raise RuntimeError(f"You have not registered the task(key:{key}) yet.")
        # 注销
        task = cls._registered_tasks.pop(key)
        # 回收进度条实例
        if key in cls._progress_bars:
            progress_bar = cls._progress_bars.pop(key)
            progress_bar.desc = "       Done"
            cls._progress_bar_pool.append(progress_bar)
        # 更新总进度条
        cls._global_progress_bar.info = {"rest": len(cls._registered_tasks)}

    @classmethod
    @synchronized(_progress_lock)
    def update(cls, key: Hashable, increment: int):
        if cls._global_progress_bar is None:
            return
        # 碰到未注册的任务信息时报错
        if key not in cls._registered_tasks:
            raise RuntimeError("Please register the task before update.")
        # 更新进度条
        task = cls._registered_tasks[key]
        if key not in cls._progress_bars:
            if len(cls._progress_bar_pool) > 0:
                new_progress_bar = cls._progress_bar_pool.popleft()
                new_progress_bar.reset()
                new_progress_bar.total = task.total
                new_progress_bar.progress = task.progress
                new_progress_bar.desc = "Downloading"
                new_progress_bar.info = task.info
            else:
                new_progress_bar = TqdmAdapter(
                    task.total,
                    initial=task.progress,
                    desc="Downloading",
                    info=task.info,
                )
            cls._progress_bars[key] = new_progress_bar
        cls._progress_bars[key].update(increment)
        cls._global_progress_bar.update(increment)
        task.progress += increment

    @classmethod
    @synchronized(_progress_lock)
    def set_total(cls, key: Hashable, total: int):
        if cls._global_progress_bar is None:
            return
        if key not in cls._registered_tasks:
            raise RuntimeError("Please register the task before set_total.")
        task = cls._registered_tasks[key]
        # 修改总进度条的total
        old_total = cls._global_progress_bar.total
        cls._global_progress_bar.total = old_total - task.total + total
        # 修改key对应的进度条的total
        if key in cls._progress_bars:
            cls._progress_bars[key].total = total
        task.total = total

    @classmethod
    @synchronized(_progress_lock)
    def set_progress(cls, key: Hashable, progress:int):
        if cls._global_progress_bar is None:
            return
        if key not in cls._registered_tasks:
            raise RuntimeError("Please register the task before set_progress.")
        task = cls._registered_tasks[key]
        # 修改总进度条的progress
        old_progress = cls._global_progress_bar.progress
        cls._global_progress_bar.progress = old_progress - task.progress + progress
        # 修改key对应的进度条的progress
        if key in cls._progress_bars:
            cls._progress_bars[key].progress = progress
        task.progress = progress

    @classmethod
    @synchronized(_progress_lock)
    def set_info(cls,key:Hashable,info:dict):
        if cls._global_progress_bar is None:
            return
        if key not in cls._registered_tasks:
            raise RuntimeError("Please register the task before set_info.")
        task = cls._registered_tasks[key]
        task.info = info
        # 修改key对应的进度条的info
        if key in cls._progress_bars:
            cls._progress_bars[key].info = info