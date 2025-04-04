import os
import pickle
from datetime import datetime
from enum import Enum

from peewee import (DatabaseProxy, Model, CharField, BlobField, DateTimeField, ForeignKeyField, IntegerField, TextField)
from playhouse.shortcuts import ThreadSafeDatabaseMetadata
from playhouse.sqlite_ext import AutoIncrementField

database = DatabaseProxy()


class Status(Enum):
    UNKNOWN = "UNKNOWN"
    DOWNLOADING = "DOWNLOADING"
    FINISHED = "FINISHED"
    ERROR = "ERROR"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class BaseModel(Model):
    class Meta:
        database = database
        model_metadata_class = ThreadSafeDatabaseMetadata

    def assign_from(self, source: "BaseModel") -> "BaseModel":
        """ 从另外一个模型中复制值 """
        for field_name in self._meta.fields:
            if hasattr(source, field_name):
                value = getattr(source, field_name)
                setattr(self, field_name, value)
        return self

    @classmethod
    def from_model(cls, model: "BaseModel") -> "BaseModel":
        return cls().assign_from(model)


class DownloadTask(BaseModel):
    id = AutoIncrementField()
    download_url = CharField()
    filename = CharField()
    save_dir = CharField(default=os.getcwd)
    file_writer_class_name = CharField(null=True)
    file_size = IntegerField(default=-1)
    dumped_callbacks = BlobField(default=pickle.dumps([], protocol=4))
    dumped_headers = TextField(default="{}")
    dumped_response_headers = TextField(default="{}")
    creation_time = DateTimeField(default=datetime.now)
    update_time = DateTimeField(default=datetime.min)


class DownloadingTask(DownloadTask):
    start_time = DateTimeField(default=datetime.now)


class Chunk(BaseModel):
    downloading_task = ForeignKeyField(DownloadingTask, on_delete="CASCADE")
    start = IntegerField()
    end = IntegerField()
    status = CharField(default=Status.UNKNOWN.value)


class CompletedDownloadTask(DownloadingTask):
    finish_time = DateTimeField(default=datetime.now)


class DeletedDownloadTask(DownloadingTask):
    delete_time = DateTimeField(default=datetime.now)
