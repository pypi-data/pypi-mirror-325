import dataclasses
import json
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path, PurePath
from typing import Any, Callable, Type

from requests.structures import CaseInsensitiveDict

from ._model import (
    BaseModel,
    Chunk,
    DownloadTask,
    Status,
)
from .. import _serialization
from .._consts import NOFILENAME
from .._typehint import StrPath


@dataclass
class BaseViewModel(ABC):

    @classmethod
    def _from_model(cls, model: BaseModel):
        """根据model创建view_model,view_model会继承model中的属性值"""
        kwargs = {}
        for _field in dataclasses.fields(cls):
            if hasattr(model, _field.name):
                value = getattr(model, _field.name)
                kwargs[_field.name] = value
        return cls(**kwargs)

    @classmethod
    @abstractmethod
    def from_model(cls, model: BaseModel):
        """根据model创建view_model,view_model会继承model中的属性值"""
        raise NotImplementedError

    def _to_model(self, model_class: Type[BaseModel]):
        """将当前view_model转换成model"""
        model = model_class()
        for attr_name in model._meta.fields:
            if hasattr(self, attr_name):
                value = getattr(self, attr_name)
                if isinstance(value, PurePath):
                    value = str(value)
                setattr(model, attr_name, value)
        return model

    @abstractmethod
    def to_model(self):
        raise NotImplementedError

    def __eq__(self,other)->bool:
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

@dataclass
class DownloadTaskViewModel(BaseViewModel):
    download_url: str
    filename: str = NOFILENAME
    save_dir: StrPath = field(default_factory=os.getcwd)
    file_writer_class_name: str = None
    callbacks: list[Callable] = field(default_factory=list)
    headers: dict = field(default_factory=dict)
    proxies: dict = field(default_factory=dict)
    response_headers: CaseInsensitiveDict = field(default_factory=CaseInsensitiveDict)
    creation_time: datetime = field(default_factory=datetime.now)
    update_time: datetime = datetime.min
    id: Any = None

    @classmethod
    def from_model(cls, model: DownloadTask) -> "DownloadTaskViewModel":
        view_model = cls._from_model(model)
        view_model.callbacks = _serialization.loads(model.dumped_callbacks)
        view_model.headers = json.loads(model.dumped_headers)
        view_model.proxies = json.loads(model.dumped_proxies)
        view_model.response_headers = CaseInsensitiveDict(
            json.loads(model.dumped_response_headers)
        )
        return view_model

    def to_model(self) -> DownloadTask:
        model = self._to_model(DownloadTask)
        model.dumped_callbacks = _serialization.dumps(self.callbacks)
        model.dumped_headers = json.dumps(self.headers)
        model.dumped_proxies = json.dumps(self.proxies)
        model.dumped_response_headers = json.dumps(dict(self.response_headers))
        return model

    @property
    def file_path(self):
        return Path(self.save_dir, self.filename)

    @property
    def file_size(self):
        if not self.response_headers:
            return 0
        return int(self.response_headers.get("Content-Length",0))

    @property
    def last_modified_time(self):
        if "last-modified" not in self.response_headers:
            return datetime.now()
        return datetime.strptime(
            self.response_headers["last-modified"], "%a, %d %b %Y %H:%M:%S %Z"
        )

    def __post_init__(self):
        if not isinstance(self.response_headers,CaseInsensitiveDict):
            self.response_headers = CaseInsensitiveDict(self.response_headers)


@dataclass
class ChunkViewModel(BaseViewModel):
    start: int
    end: int
    status: str = Status.UNKNOWN.value
    downloaded_size: int = 0
    downloading_task: DownloadTaskViewModel = None
    id: Any = None

    @classmethod
    def from_model(cls, chunk: Chunk) -> "ChunkViewModel":
        view_model = cls._from_model(chunk)
        if chunk.downloading_task is not None:
            view_model.downloading_task = DownloadingTaskViewModel.from_model(
                chunk.downloading_task
            )
        return view_model

    def to_model(self) -> Chunk:
        model = self._to_model(Chunk)
        if self.downloading_task is not None:
            model.downloading_task = self.downloading_task.to_model()
        return model

    @property
    def range_headers(self):
        headers = {"Range": f"bytes={self.start+self.downloaded_size}-{self.end}"}
        return headers

    @property
    def size(self):
        return self.end - self.start + 1


@dataclass
class DownloadingTaskViewModel(DownloadTaskViewModel):
    chunks: list[ChunkViewModel] = field(default_factory=list)
    start_time: datetime = field(default_factory=datetime.now)


@dataclass
class DeletedDownloadTaskViewModel(DownloadTaskViewModel):
    delete_time: datetime = field(default_factory=datetime.now)


@dataclass
class CompletedDownloadTaskViewModel(DownloadingTaskViewModel):
    finish_time: datetime = field(default_factory=datetime.now)
