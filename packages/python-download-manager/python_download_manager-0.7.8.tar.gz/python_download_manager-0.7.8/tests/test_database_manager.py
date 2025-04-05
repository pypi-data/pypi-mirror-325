import inspect
import random
import shutil
import tempfile
import time
import unittest
from pathlib import Path

from python_download_manager import _utility
from python_download_manager._consts import MB, GB
from python_download_manager._database import _model
from python_download_manager._database._database_manager import DatabaseManager
from python_download_manager._database._model import (
    BaseModel,
    Chunk,
    DownloadTask,
    DownloadingTask,
    DeletedDownloadTask,
    CompletedDownloadTask,
    Status,
)
from python_download_manager._database._viewmodel import (
    ChunkViewModel,
    DownloadTaskViewModel,
    DownloadingTaskViewModel,
    DeletedDownloadTaskViewModel,
    CompletedDownloadTaskViewModel,
)


class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        # 临时目录
        self.temp_dir = tempfile.mkdtemp()
        # 初始化数据库
        DatabaseManager.initialize(self.temp_dir)
        # 块大小
        self.chunk_size = random.randint(4 * MB, 16 * MB)

        # 随机生成若干个等待下载的任务
        self.download_tasks = []
        for i in range(random.randint(5, 10)):
            random_task = DownloadingTaskViewModel(
                download_url=f"https://random.download.url/{time.time_ns()}",
                filename=f"random_filename_{time.time_ns()}.file",
            )
            added_task = DatabaseManager.add_download_task(random_task)
            self.download_tasks.append(added_task)

        # 随机生成若干个下载中的任务
        self.downloading_tasks = []
        for i in range(random.randint(5, 10)):
            random_task = DownloadingTaskViewModel(
                download_url=f"https://random.download.url/{time.time_ns()}",
                filename=f"random_filename_{time.time_ns()}.file",
            )
            added_task = DatabaseManager.add_download_task(random_task)
            chunks = _utility.slice_file(added_task.file_size, self.chunk_size)
            downloading_task, _ = DatabaseManager.start_download_task(
                added_task, chunks
            )
            self.downloading_tasks.append(downloading_task)

        # 随机生成若干个已完成的任务
        self.completed_tasks = []
        for i in range(random.randint(5, 10)):
            random_task = DownloadingTaskViewModel(
                download_url=f"https://random.download.url/{time.time_ns()}",
                filename=f"random_filename_{time.time_ns()}.file",
            )
            added_task = DatabaseManager.add_download_task(random_task)
            chunks = _utility.slice_file(added_task.file_size, self.chunk_size)
            downloading_task, _ = DatabaseManager.start_download_task(
                added_task, chunks
            )
            completed_task = DatabaseManager.complete_download_task(downloading_task)
            self.completed_tasks.append(completed_task)

        # 随机生成若干个已删除的下载任务
        random_tasks = []
        for i in range(random.randint(5, 10)):
            random_task = DownloadingTaskViewModel(
                download_url=f"https://random.download.url/{time.time_ns()}",
                filename=f"random_filename_{time.time_ns()}.file",
            )
            added_task = DatabaseManager.add_download_task(random_task)
            random_tasks.append(added_task)
        self.deleted_tasks = DatabaseManager.delete_download_tasks(
            [task.id for task in random_tasks]
        )

        # # 随机选一个生成的下载任务用作一般测试
        # self.download_task = random.choice(self.download_tasks)
        # # 分割文件块
        # self.chunk_size = random.randint(4 * MB, 8 * MB)
        # self.chunks = utility.slice_file(self.download_task.file_size, self.chunk_size)

    def tearDown(self):
        DatabaseManager.close()
        shutil.rmtree(self.temp_dir)

    def test__init__(self):
        """测试：初始化"""
        # 检查数据库文件是否存在
        db_file_path = Path(self.temp_dir, DatabaseManager.DB_FILENAME)
        self.assertTrue(
            db_file_path.exists(), f"The DB_FILE should exist in {self.temp_dir}"
        )
        # 检查表是否存在
        for model_name, model_cls in inspect.getmembers(
            _model,
            lambda m: inspect.isclass(m)
            and issubclass(m, BaseModel)
            and m is not BaseModel,
        ):
            self.assertTrue(
                model_cls.table_exists(), f"{model_name}'s table doesn't exist"
            )

    def test_add_download_task(self):
        """测试：添加下载任务"""
        # 添加下载任务
        task = DownloadTaskViewModel(
            download_url="test_add_download_task",
            file_writer_class_name="MultiPartFileWriter",
            filename="test_filename.ext",
        )
        added_task = DatabaseManager.add_download_task(task)
        self.assertIs(
            type(added_task),
            DownloadTaskViewModel,
            "The method's return type should be DownloadTaskViewModel",
        )

        is_existing = (
            DownloadTask.select().where(DownloadTask.id == added_task.id).exists()
        )
        self.assertTrue(is_existing, "download_task should exist after it is added")

    def test_complete_download_task(self):
        """测试：完成下载任务"""
        for downloading_task in self.downloading_tasks:
            # 完成下载任务
            completed_task = DatabaseManager.complete_download_task(downloading_task)
            # 返回值应为CompletedDownloadTaskViewModel
            self.assertIs(
                type(completed_task),
                CompletedDownloadTaskViewModel,
                f"The method's return type should be {CompletedDownloadTaskViewModel.__name__}",
            )
            # 下载中的任务数应当不存在
            task_existing = (
                DownloadingTask.select()
                .where(DownloadingTask.id == downloading_task.id)
                .exists()
            )
            self.assertFalse(
                task_existing, f"task should not exist after it is completed"
            )
            # 任务对应的文件块记录应当被级联删除
            chunks_existing = (
                Chunk.select()
                .where(Chunk.downloading_task == completed_task.id)
                .exists()
            )
            self.assertFalse(
                chunks_existing,
                "chunks should not exists after downloading task is completed",
            )
            # 刚刚完成的任务应该能从历史表中查到
            is_existing = (
                CompletedDownloadTask.select()
                .where(CompletedDownloadTask.id == completed_task.id)
                .exists()
            )
            self.assertTrue(
                is_existing,
                f"completed_task should exist after download_task is completed",
            )

    def test_delete_completed_tasks_no_args(self):
        """测试：删除所有已完成的下载任务"""
        deleted_tasks = DatabaseManager.delete_completed_tasks()
        # 被删除的任务数量应当和已完成的任务数量一样
        self.assertEqual(
            len(deleted_tasks),
            len(self.completed_tasks),
            "The number of deleted tasks should be equal to the number of completed tasks.",
        )
        # 已完成的下载任务数量应当为0
        rows_count = CompletedDownloadTask.select().count()
        self.assertEqual(
            rows_count,
            0,
            "The rows count of CompletedTask should be 0 after it's truncated.",
        )

    def test_delete_completed_tasks_with_args(self):
        """测试：随机删除若干个已完成的任务"""
        # 随机选几个任务
        random_ids = {task.id for task in random.choices(self.completed_tasks, k=5)}
        # 删除任务
        deleted_tasks = DatabaseManager.delete_completed_tasks(random_ids)
        # 被删除的任务的数量应当和被选出来的任务数量一致
        self.assertEqual(
            len(deleted_tasks),
            len(random_ids),
            "The number of deleted tasks should be equal to the number of completed tasks that were chosen.",
        )
        # 被删除的任务应当不存在
        existing = (
            CompletedDownloadTask.select()
            .where(CompletedDownloadTask.id << random_ids)
            .exists()
        )
        self.assertFalse(
            existing, "The completed tasks should not exist after it is deleted."
        )
        # 检查剩下的任务数量是否正确
        left_task_count = (
            CompletedDownloadTask.select()
            .where(~CompletedDownloadTask.id << random_ids)
            .count()
        )
        self.assertEqual(left_task_count, len(self.completed_tasks) - len(random_ids))

    def test_delete_deleted_tasks_no_args(self):
        """测试：清空回收站中的任务"""
        deleted_tasks = DatabaseManager.delete_deleted_tasks()
        # 被删除的任务数量应当和回收站中的任务数量一致
        self.assertEqual(
            len(deleted_tasks),
            len(self.deleted_tasks),
            "The number of deleted tasks that were deleted should be equal to the number of deleted task.",
        )
        # 清空后，回收站中的任务数量应当为0
        rows_count = DeletedDownloadTask.select().count()
        self.assertEqual(
            rows_count,
            0,
            "The rows count of DeletedDownloadTask should be 0 after the table was truncated.",
        )

    def test_delete_deleted_tasks_with_args(self):
        """测试：随机删除若干个回收站中的任务"""
        # 随机选几个要删除的任务
        random_ids = {task.id for task in random.choices(self.deleted_tasks, k=5)}
        # 删除回收站的若干个任务
        deleted_tasks = DatabaseManager.delete_deleted_tasks(random_ids)
        # 被删除的任务数量应当等同于被随机选出来的数量
        self.assertEqual(
            len(deleted_tasks),
            len(random_ids),
            "The number of deleted tasks that were deleted should be equal to the number of deleted task that were chosen.",
        )
        # 被删除的任务应当不存在
        existing = (
            DeletedDownloadTask.select()
            .where(DeletedDownloadTask.id << random_ids)
            .exists()
        )
        self.assertFalse(
            existing, "The deleted tasks should not exist after they were deleted."
        )
        # 检查回收站中剩下的任务数量
        left_task_count = (
            DeletedDownloadTask.select()
            .where(~DeletedDownloadTask.id << random_ids)
            .count()
        )
        self.assertEqual(left_task_count, len(self.deleted_tasks) - len(random_ids))

    def test_delete_download_tasks_no_args(self):
        """测试：将所有等待中的任务清空并放入回收站"""
        deleted_tasks = DatabaseManager.delete_download_tasks()
        # 被清空的任务数量要和等待中的任务数量一致
        self.assertEqual(
            len(deleted_tasks),
            len(self.download_tasks),
            "The number of deleted tasks should be equal to the number of download tasks in waiting.",
        )
        # 清空后，等待中的任务数量应当为0
        download_task_count = DownloadTask.select().count()
        self.assertEqual(
            download_task_count,
            0,
            "The number of download task should be 0 after the table was truncated.",
        )
        # 放入回收站后，回收站中应当存在相应的记录
        task_ids = {task.id for task in self.download_tasks}
        deleted_tasks = DeletedDownloadTask.select().where(
            DeletedDownloadTask.id << task_ids
        )
        deleted_task_ids = {task.id for task in deleted_tasks}
        self.assertEqual(
            deleted_task_ids, task_ids, "The deleted_task_ids should equal the task_ids"
        )

    def test_delete_download_tasks_with_args(self):
        """测试：随机删除几个等待中的下载任务，并放入回收站"""
        random_ids = {task.id for task in random.choices(self.download_tasks, k=5)}
        deleted_tasks = DatabaseManager.delete_download_tasks(random_ids)
        # 被删除的任务数量应当与被随机选出来的任务数量一致
        self.assertEqual(
            len(deleted_tasks),
            len(random_ids),
            "The number of deleted tasks should be equal to the number of download task in waiting that was chosen.",
        )
        # 被删除的任务应当不存在
        existing = DownloadTask.select().where(DownloadTask.id << random_ids).exists()
        self.assertFalse(
            existing, "The download tasks should not exist after they were deleted."
        )
        # 检查剩下的任务数量是否匹配
        left_task_count = (
            DownloadTask.select().where(~DownloadTask.id << random_ids).count()
        )
        self.assertEqual(left_task_count, len(self.download_tasks) - len(random_ids))
        # 回收站中应当存在被删除的任务
        deleted_tasks = DeletedDownloadTask.select().where(
            DeletedDownloadTask.id << random_ids
        )
        deleted_task_ids = {task.id for task in deleted_tasks}
        self.assertEqual(
            deleted_task_ids,
            random_ids,
            "The deleted_task_ids should equal the random_ids",
        )

    def test_delete_download_tasks_forever(self):
        """测试：永久删除等待中的下载任务"""
        deleted_tasks = DatabaseManager.delete_download_tasks(forever=True)
        # 永久删除后，回收站中应当不存在相应的记录
        deleted_task_ids = {task.id for task in deleted_tasks}
        existing = (
            DeletedDownloadTask.select()
            .where(DeletedDownloadTask.id << deleted_task_ids)
            .exists()
        )
        self.assertFalse(
            existing,
            "The download tasks should not exists after they were deleted forever.",
        )

    def test_delete_downloading_tasks_no_args(self):
        """测试：清空下载中的任务，并放入回收站"""
        deleted_tasks = DatabaseManager.delete_downloading_tasks()
        # 被清空的任务数量应当与下载中的任务数量一致
        self.assertEqual(
            len(deleted_tasks),
            len(self.downloading_tasks),
            "The number of tasks that were deleted should be equal to the number of downlaoding tasks.",
        )
        # 清空后下载中的任务数量应当为0
        downloading_task_count = DownloadingTask.select().count()
        self.assertEqual(
            downloading_task_count,
            0,
            "The number of downloading task should be 0 after the table was truncated.",
        )
        # 清空后，文件块的数量应当为0
        chunks_count = Chunk.select().count()
        self.assertEqual(
            chunks_count,
            0,
            "The number of chunks should be 0 after the downloading task table was truncated.",
        )
        # 放入回收站后，回收站内应当存在相应的记录
        downloading_task_ids = {task.id for task in self.downloading_tasks}
        deleted_tasks = DeletedDownloadTask.select().where(
            DeletedDownloadTask.id << downloading_task_ids
        )
        deleted_task_ids = {task.id for task in deleted_tasks}
        self.assertEqual(
            downloading_task_ids,
            deleted_task_ids,
            "The downloading_task_ids should be equal to the deleted_task_ids",
        )

    def test_delete_downloading_tasks_with_args(self):
        """测试：随机删除若干个下载中的任务"""
        random_ids = {task.id for task in random.choices(self.downloading_tasks, k=5)}
        deleted_tasks = DatabaseManager.delete_downloading_tasks(random_ids)
        # 被删除的任务数量应当与被随机选出来的任务数量一致
        self.assertEqual(
            len(deleted_tasks),
            len(random_ids),
            "The number of deleted tasks should be equal to the number of download task in waiting that was chosen.",
        )
        # 被删除的任务应当不存在
        existing = (
            DownloadingTask.select().where(DownloadingTask.id << random_ids).exists()
        )
        self.assertFalse(
            existing, "The download tasks should not exist after they were deleted."
        )
        # 与被删除的任务相关的文件块应当不存在
        chunks_existing = (
            Chunk.select().where(Chunk.downloading_task << random_ids).exists()
        )
        self.assertFalse(
            chunks_existing,
            "The chunks correspond with downloading task should not exist.",
        )
        # 检查剩下的任务数量是否匹配
        left_task_count = (
            DownloadingTask.select().where(~DownloadingTask.id << random_ids).count()
        )
        self.assertEqual(left_task_count, len(self.downloading_tasks) - len(random_ids))
        # 回收站中应当存在被删除的任务
        deleted_tasks = DeletedDownloadTask.select().where(
            DeletedDownloadTask.id << random_ids
        )
        deleted_task_ids = {task.id for task in deleted_tasks}
        self.assertEqual(
            deleted_task_ids,
            random_ids,
            "The deleted_task_ids should equal the random_ids",
        )

    def test_delete_downloading_tasks_forever(self):
        """测试：永久删除下载中的任务"""
        deleted_tasks = DatabaseManager.delete_downloading_tasks(forever=True)
        # 永久删除后，回收站中应当不存在相应的记录
        deleted_task_ids = {task.id for task in deleted_tasks}
        existing = (
            DeletedDownloadTask.select()
            .where(DeletedDownloadTask.id << deleted_task_ids)
            .exists()
        )
        self.assertFalse(
            existing,
            "The downloading tasks should not exists after they were deleted forever.",
        )
        # 永久删除后，相应的文件块应当不存在
        deleted_task_ids = {task.id for task in deleted_tasks}
        chunks_existing = (
            Chunk.select().where(Chunk.downloading_task << deleted_task_ids).exists()
        )
        self.assertFalse(
            chunks_existing,
            "The chunks should not exist after the downloading tasks were deleted.",
        )

    def test_get_all_downloading_task_chunks(self):
        """测试：获取某个下载中的任务的所有文件块"""
        for downloading_task in self.downloading_tasks:
            # 获取文件块
            downloading_task_chunks = DatabaseManager.get_all_downloading_task_chunks(
                downloading_task
            )
            # 文件块的数量不应当为0
            self.assertNotEqual(
                len(downloading_task_chunks), 0, "The number of chunks should not be 0"
            )
            # 检查文件块的数量
            sliced_chunks = _utility.slice_file(
                downloading_task.file_size, self.chunk_size
            )
            self.assertEqual(
                len(sliced_chunks),
                len(downloading_task_chunks),
                "The number of chunks is not correct.",
            )
            # 所有的文件块的类型都应为ChunkViewModel
            for downloading_task_chunk in downloading_task_chunks:
                self.assertIs(type(downloading_task_chunk), ChunkViewModel)

    def test_get_all_download_task(self):
        """测试：获取所有下载任务"""
        tasks = DatabaseManager.get_all_download_task()
        rows_count = DownloadTask.select().count()
        # 检查数量
        self.assertEqual(len(tasks), rows_count, "len(tasks) should equal rows_count")
        # 检查是否相等
        for task in tasks:
            self.assertIs(type(task), DownloadTaskViewModel)

    def test_get_all_download_task_with_args(self):
        """测试：获取部分下载任务"""
        random_tasks = random.choices(self.download_tasks, k=5)
        task_ids = {task.id for task in random_tasks}
        tasks = DatabaseManager.get_all_download_task(task_ids)
        # 检查数量
        self.assertEqual(len(tasks), len(task_ids), "len(tasks) should equal rows_count")

    def test_get_all_downloading_task(self):
        """测试：获取所有下载中的任务"""
        tasks = DatabaseManager.get_all_downloading_task()
        rows_count = DownloadingTask.select().count()
        # 检查数量
        self.assertEqual(len(tasks), rows_count, "len(tasks) should equal rows_count")
        # 检查是否相等
        for task in tasks:
            self.assertIs(type(task), DownloadingTaskViewModel)

    def test_get_all_downloading_task_with_args(self):
        """测试：获取部分下载中的任务"""
        random_tasks = random.choices(self.downloading_tasks, k=5)
        task_ids = {task.id for task in random_tasks}
        tasks = DatabaseManager.get_all_downloading_task(task_ids)
        # 检查数量
        self.assertEqual(len(tasks), len(task_ids), "len(tasks) should equal rows_count")

    def test_get_all_deleted_download_task(self):
        """测试：获取所有已删除的下载任务"""
        deleted_tasks = DatabaseManager.get_all_deleted_download_task()
        rows_count = DeletedDownloadTask.select().count()
        self.assertEqual(
            len(deleted_tasks), rows_count, "len(deleted_tasks) should equal rows_count"
        )
        for task in deleted_tasks:
            self.assertIs(type(task), DeletedDownloadTaskViewModel)

    def test_get_all_deleted_download_task_with_args(self):
        """测试：获取部分下载任务"""
        random_tasks = random.choices(self.deleted_tasks, k=5)
        task_ids = {task.id for task in random_tasks}
        tasks = DatabaseManager.get_all_deleted_download_task(task_ids)
        # 检查数量
        self.assertEqual(len(tasks), len(task_ids), "len(tasks) should equal rows_count")

    def test_get_all_completed_download_task(self):
        """测试：获取所有已完成的下载任务"""
        completed_tasks = DatabaseManager.get_all_completed_download_task()
        rows_count = CompletedDownloadTask.select().count()
        self.assertEqual(
            len(completed_tasks),
            rows_count,
            "len(completed_tasks) should equal the rows_count",
        )
        for task in completed_tasks:
            self.assertIs(type(task), CompletedDownloadTaskViewModel)

    def test_get_all_completed_download_task_with_args(self):
        """测试：获取部分下载任务"""
        random_tasks = random.choices(self.completed_tasks, k=5)
        task_ids = {task.id for task in random_tasks}
        tasks = DatabaseManager.get_all_completed_download_task(task_ids)
        # 检查数量
        self.assertEqual(len(tasks), len(task_ids), "len(tasks) should equal rows_count")

    def test_start_download(self):
        """测试：开始下载"""
        for download_task in self.download_tasks:
            chunks = _utility.slice_file(download_task.file_size, self.chunk_size)
            # 开始下载
            downloading_task, added_chunks = DatabaseManager.start_download_task(
                download_task, chunks
            )
            # 测试返回值类型
            self.assertIs(type(downloading_task), DownloadingTaskViewModel)
            for chunk in added_chunks:
                self.assertIs(type(chunk), ChunkViewModel)
            # 开始下载后，任务不应当存在于任务表中
            download_task_existing = (
                DownloadTask.select()
                .where(DownloadTask.id == download_task.id)
                .exists()
            )
            self.assertFalse(
                download_task_existing,
                "The download task should not exist after it is started",
            )
            # 开始下载后，下载中的任务表中应当有相应的记录
            downloading_task_existing = (
                DownloadingTask.select()
                .where(DownloadingTask.id == downloading_task.id)
                .exists()
            )
            self.assertTrue(
                downloading_task_existing,
                "The downloading task should exist after download task is started",
            )
            # 返回的文件块列表长度应当与插入时的列表长度一致
            self.assertEqual(
                len(chunks),
                len(added_chunks),
                "The length of added chunks should equal the length of chunks",
            )
            # 开始下载后，数据库中应当存在相应的文件块记录
            rows_count = (
                Chunk.select()
                .where(Chunk.downloading_task == downloading_task.id)
                .count()
            )
            self.assertEqual(
                len(chunks),
                rows_count,
                f"len(chunks){len(chunks)} not equal rows_count({rows_count})",
            )

    def test_update_chunk(self):
        """测试：更新文件块"""
        for downloading_task in self.downloading_tasks:
            chunks = DatabaseManager.get_all_downloading_task_chunks(downloading_task)
            # 随机进行5-10次测试，每次随机选一个文件块，每次随机设置成一个状态
            status_list = [member.value for member in Status._member_map_.values()]
            for i in range(random.randrange(5, 11)):
                random_chunk = random.choice(chunks)
                random_status = random.choice(status_list)
                random_chunk.status = random_status
                updated_chunk = DatabaseManager.update_chunk(random_chunk)
                self.assertIs(type(updated_chunk), ChunkViewModel)
                # 检查更新后的结果是否正确
                updated_chunk_model = Chunk.get_by_id(random_chunk.id)
                updated_chunk = ChunkViewModel.from_model(updated_chunk_model)
                self.assertEqual(random_chunk, updated_chunk, "update fail")
