import inspect
from pathlib import Path
from threading import Lock

from peewee import SqliteDatabase

from . import _model
from ._model import (
    database,
    BaseModel,
    Chunk,
    DownloadTask,
    DownloadingTask,
    DeletedDownloadTask,
    CompletedDownloadTask,
)
from ._viewmodel import (
    ChunkViewModel,
    DownloadTaskViewModel,
    DownloadingTaskViewModel,
    DeletedDownloadTaskViewModel,
    CompletedDownloadTaskViewModel,
)
from .._decorators import synchronized
from .._typehint import StrPath

# 写入锁，防止多个线程同时对数据库进行写入
_write_lock = Lock()


class DatabaseManager:
    DB_FILENAME = "python_download_manager.db"
    _initialized = False

    @classmethod
    def initialize(cls, database_dir: StrPath = None):
        if cls._initialized:
            return
        if not database_dir:
            database_dir = ".pdm"
        if database_dir == ":memory:":
            database_file_path = database_dir
        else:
            database_file_path = Path(database_dir, cls.DB_FILENAME)
            database_file_path.parent.mkdir(parents=True, exist_ok=True)
        # 初始化数据库
        database.initialize(
            SqliteDatabase(
                database_file_path,
                pragmas={"foreign_keys": 1, "journal_mode": "wal"},
            )
        )
        # 创建表(当表不存在时)
        member_items = inspect.getmembers(
            _model,
            lambda m: inspect.isclass(m)
            and issubclass(m, BaseModel)
            and m is not BaseModel,
        )
        model_classes = [model_class for _, model_class in member_items]
        database.create_tables(model_classes)
        cls._initialized = True

    @staticmethod
    @synchronized(_write_lock)
    def add_download_task(
        download_task: DownloadTaskViewModel,
    ) -> DownloadTaskViewModel:
        """添加下载任务"""
        task_model = download_task.to_model()
        task_model.save()
        return DownloadTaskViewModel.from_model(task_model)

    @classmethod
    def close(cls):
        if not cls._initialized:
            return
        database.close()
        cls._initialized = False

    @staticmethod
    @synchronized(_write_lock)
    @database.atomic()
    def delete_completed_tasks(
        task_ids: list[int] = None,
    ) -> list[CompletedDownloadTaskViewModel]:
        """批量删除已完成的下载任务，如果传入的参数为None，则删除表中的所有数据"""
        if task_ids is None:
            tasks = list(CompletedDownloadTask.select())
            CompletedDownloadTask.truncate_table()
        else:
            tasks = list(
                CompletedDownloadTask.select().where(
                    CompletedDownloadTask.id << task_ids
                )
            )
            CompletedDownloadTask.delete().where(
                CompletedDownloadTask.id << task_ids
            ).execute()
        return [CompletedDownloadTaskViewModel.from_model(task) for task in tasks]

    @staticmethod
    @synchronized(_write_lock)
    @database.atomic()
    def delete_deleted_tasks(
        task_ids: list[int] = None,
    ) -> list[DeletedDownloadTaskViewModel]:
        """批量删除回收站中的下载任务，如果传入的参数为None，则删除表中的所有数据"""
        if task_ids is None:
            tasks = list(DeletedDownloadTask.select())
            DeletedDownloadTask.truncate_table()
        else:
            tasks = list(
                DeletedDownloadTask.select().where(DeletedDownloadTask.id << task_ids)
            )
            DeletedDownloadTask.delete().where(
                DeletedDownloadTask.id << task_ids
            ).execute()
        return [DeletedDownloadTask.from_model(task) for task in tasks]

    @staticmethod
    @synchronized(_write_lock)
    @database.atomic()
    def delete_download_tasks(
        task_ids: list[int] = None, forever: bool = False
    ) -> list[DownloadTaskViewModel]:
        """批量删除下载任务，如果传入的参数为None，则删除表中的所有数据"""
        if task_ids is None:
            tasks = list(DownloadTask.select())
            DownloadTask.truncate_table()
        else:
            tasks = list(DownloadTask.select().where(DownloadTask.id << task_ids))
            DownloadTask.delete().where(DownloadTask.id << task_ids).execute()
        if not forever:
            deleted_tasks = [
                DeletedDownloadTask.from_model(task).__data__ for task in tasks
            ]
            DeletedDownloadTask.insert_many(deleted_tasks).execute()
        return [DownloadTaskViewModel.from_model(task) for task in tasks]

    @staticmethod
    @synchronized(_write_lock)
    @database.atomic()
    def delete_downloading_tasks(
        task_ids: list[int] = None, forever: bool = False
    ) -> list[DownloadingTaskViewModel]:
        """批量删除下载中的任务，如果传入的参数为None，则删除表中的所有数据"""
        if task_ids is None:
            tasks = list(DownloadingTask.select())
            DownloadingTask.truncate_table()
        else:
            tasks = list(DownloadingTask.select().where(DownloadingTask.id << task_ids))
            DownloadingTask.delete().where(DownloadingTask.id << task_ids).execute()
        if not forever:
            deleted_tasks = [
                DeletedDownloadTask.from_model(task).__data__ for task in tasks
            ]
            DeletedDownloadTask.insert_many(deleted_tasks).execute()
        return [DownloadingTaskViewModel.from_model(task) for task in tasks]

    @staticmethod
    @synchronized(_write_lock)
    @database.atomic()
    def complete_download_task(
        downloading_task: DownloadingTaskViewModel,
    ) -> CompletedDownloadTaskViewModel:
        """完成下载任务"""
        task = DownloadingTask.get_by_id(downloading_task.id)
        task.delete_instance()
        completed_task = CompletedDownloadTask().assign_from(task)
        completed_task.save(force_insert=True)
        return CompletedDownloadTaskViewModel.from_model(completed_task)

    @staticmethod
    def get_all_downloading_task_chunks(
        downloading_task: DownloadingTaskViewModel,
    ) -> list[ChunkViewModel]:
        """获取某个下载中的任务的所有文件块"""
        chunks = Chunk.select().where(Chunk.downloading_task == downloading_task.id)
        return [ChunkViewModel.from_model(chunk) for chunk in chunks]

    @staticmethod
    def get_all_download_task(task_ids: list = None) -> list[DownloadTaskViewModel]:
        """获取所有下载任务"""
        if task_ids:
            tasks = DownloadTask.select().where(DownloadTask.id << task_ids)
        else:
            tasks = DownloadTask.select()
        return [DownloadTaskViewModel.from_model(task) for task in tasks]

    @staticmethod
    def get_all_downloading_task(
        task_ids: list = None,
    ) -> list[DownloadingTaskViewModel]:
        if task_ids:
            tasks = DownloadingTask.select().where(DownloadingTask.id << task_ids)
        else:
            tasks = DownloadingTask.select()
        return [DownloadingTaskViewModel.from_model(task) for task in tasks]

    @staticmethod
    def get_all_deleted_download_task(
        task_ids: list = None,
    ) -> list[DeletedDownloadTaskViewModel]:
        """获取所有已删除的下载任务"""
        if task_ids:
            tasks = DeletedDownloadTask.select().where(
                DeletedDownloadTask.id << task_ids
            )
        else:
            tasks = DeletedDownloadTask.select()
        return [DeletedDownloadTaskViewModel.from_model(task) for task in tasks]

    @staticmethod
    def get_all_completed_download_task(
        task_ids: list = None,
    ) -> list[CompletedDownloadTaskViewModel]:
        """获取所有已完成的下载任务"""
        if task_ids:
            tasks = CompletedDownloadTask.select().where(
                CompletedDownloadTask.id << task_ids
            )
        else:
            tasks = CompletedDownloadTask.select()
        return [CompletedDownloadTaskViewModel.from_model(task) for task in tasks]

    @staticmethod
    @synchronized(_write_lock)
    @database.atomic()
    def start_download_task(
        download_task: DownloadTaskViewModel, chunks: list[ChunkViewModel]
    ) -> (DownloadingTaskViewModel, list[Chunk]):
        """将任务标记为下载中，并添加下载中任务的文件块信息"""
        # 将任务移动到下载任务表中
        task = download_task.to_model()
        task.delete_instance()
        downloading_task = DownloadingTask().assign_from(task)
        downloading_task.save(force_insert=True)
        # 插入文件块信息
        rows = []
        for chunk in chunks:
            chunk_model = chunk.to_model()
            chunk_model.downloading_task = downloading_task
            rows.append(chunk_model.__data__)
        Chunk.insert_many(rows).execute()
        # 将插入后的数据返回
        downloading_task = DownloadingTaskViewModel.from_model(downloading_task)
        chunk_models = Chunk.select().where(
            Chunk.downloading_task == downloading_task.id
        )
        chunks = [ChunkViewModel.from_model(chunk) for chunk in chunk_models]
        return downloading_task, chunks

    @staticmethod
    @synchronized(_write_lock)
    def update_chunk(chunk: ChunkViewModel) -> ChunkViewModel:
        """更新文件块"""
        chunk_model = chunk.to_model()
        chunk_model.downloading_task = chunk.downloading_task.id
        chunk_model.save()
        return chunk

    @staticmethod
    @synchronized(_write_lock)
    def update_download_task(
        download_task: DownloadTaskViewModel,
    ) -> DownloadTaskViewModel:
        task_model = download_task.to_model()
        task_model.save()
        return download_task
