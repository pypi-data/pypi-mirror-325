from abc import ABC
from collections import deque
from threading import Lock
from typing import Hashable, Type

from .adapter import ProgressAdapter, TqdmAdapter
from ..decorators import synchronized

_progress_lock = Lock()


class ProgressManager(ABC):
    auto_unregister = False
    repeat_use = False
    _progresses: dict[Hashable, ProgressAdapter] = {}
    _progress_pool: deque[ProgressAdapter] = deque()
    _progress_class: Type[TqdmAdapter] = None

    @classmethod
    @synchronized(_progress_lock)
    def register(cls, key: Hashable, total: int, info: dict = None) -> ProgressAdapter:
        if cls.repeat_use and len(cls._progress_pool) > 0:
            progress = cls._progress_pool.popleft()
            progress.set_info(info or {})
        else:
            progress = cls._progress_class(total, info)
        cls._progresses[key] = progress
        return progress

    @classmethod
    @synchronized(_progress_lock)
    def unregister(cls, key: Hashable) -> ProgressAdapter:
        # if key not in cls._progresses:
        #     return None
        progress = cls._progresses.pop(key)
        if cls.repeat_use:
            cls.write_message(f"done:{key}")
            progress.reset()
            cls._progress_pool.append(progress)
        else:
            progress.close()
        return progress

    @classmethod
    @synchronized(_progress_lock)
    def update(cls, key: Hashable, increase: int):
        # if key not in cls._progresses:
        #     return
        progress = cls._progresses[key]
        progress.update(increase)
        if progress.pos >= progress.total and cls.auto_unregister:
            cls.unregister(key)

    @classmethod
    def write_message(cls, message: str):
        cls._progress_class.write_message(message)


class TqdmProgressManager(ProgressManager):
    _progress_class = TqdmAdapter
