import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

from ._database import DownloadTask
from ._download_manager import DownloadManager

# 工作目录
_work_dir = Path(tempfile.gettempdir(), ".pdm")
_download_manager = None


def add_download_task(url: str, filename: str = None, save_dir: str = None):
    """添加下载任务"""
    save_dir = save_dir or "."
    _download_manager.add_download_task(url, filename=filename, save_dir=save_dir)


def start_download():
    _download_manager.start()
    _download_manager.wait()


def print_tasks(tasks: list[DownloadTask]):
    print("task_id \t filename \t dir \t url")
    print("--------------------------------------------------")
    for task in tasks:
        print(f"{task.id}\t{task.filename}\t{task.save_dir}\t{task.download_url}")


# region 与cli直接对接的方法


def __batch(urls: list[str], dir: str):
    for url in urls:
        add_download_task(url, filename=None, save_dir=dir)
    start_download()


def __clear():
    shutil.rmtree(_work_dir)


def __download(url: str, filename: str, dir: str):
    add_download_task(url, filename, dir)
    start_download()


def __delete(status: str, task_ids: list[int], forever: bool):
    # 确认是否删除所有任务
    if len(task_ids) == 0:
        print(f"All {status} task will be deleted, please input 'Yes' to continue.")
        user_cancelled = (
                input("Press enter directly to cancel this operation: ") != "Yes"
        )
        if user_cancelled:
            print("Cancel delete.")
            return
        task_ids = None
    # 确认是否永久删除
    forever = status in ["deleted", "completed"] or forever
    if forever:
        print("Tasks will be deleted FOREVER,please input 'Yes' to continue.")
        user_cancelled = (
                input("Press enter directly to cancel this operation: ") != "Yes"
        )
        if user_cancelled:
            print("Cancel delete.")
            return
    if status == "waiting":
        deleted_tasks = _download_manager.delete_download_tasks(task_ids, forever)
    elif status == "downloading":
        deleted_tasks = _download_manager.delete_downloading_tasks(task_ids, forever)
    elif status == "deleted":
        deleted_tasks = _download_manager.delete_deleted_tasks(task_ids)
    elif status == "completed":
        deleted_tasks = _download_manager.delete_completed_tasks(task_ids)
    print_tasks(deleted_tasks)
    print(f"Above tasks has been deleted{' FOREVER' if forever else ''}.")


def __list(status: str):
    if status == "waiting":
        tasks = _download_manager.get_all_download_task()
    elif status == "downloading":
        tasks = _download_manager.get_all_downloading_task()
    elif status == "deleted":
        tasks = _download_manager.get_all_deleted_task()
    elif status == "completed":
        tasks = _download_manager.get_all_completed_task()
    print_tasks(tasks)


def __resume():
    start_download()

def __stop():
    _download_manager.stop()

# endregion


def execute(args):
    this_module = sys.modules[__name__]
    method = getattr(this_module, f"__{args.command}")
    kwargs = args.__dict__.copy()
    kwargs.pop("command")
    method(**kwargs)


def e(parser: argparse.ArgumentParser):
    while True:
        user_input = input("(pdm) >>> ")
        if user_input == "" or "█" in user_input:
            continue
        if user_input == "exit":
            break
        args = parser.parse_args(re.split(r"\s+", user_input))
        execute(args)


def cli():
    """命令行接口"""
    global _download_manager
    # 初始化下载管理器
    _download_manager = DownloadManager(_work_dir)
    # 参数解析器
    parser = argparse.ArgumentParser(description="Python Download Manager")
    parser.add_argument("-v", "--version", action="version", version="1.0.0")
    subparser = parser.add_subparsers(title="batch download", dest="command")

    # 清理数据库
    subparser.add_parser("clear", help="清理数据库")

    # 单个下载的参数
    download_parser = subparser.add_parser("download", help="单个下载")
    download_parser.add_argument("url", help="下载链接")
    download_parser.add_argument(
        "-f", "--filename", help="文件名，缺省时会从下载链接中提取"
    )
    download_parser.add_argument("-d", "--dir", help="下载目录")

    # 批量下载的参数
    batch_parser = subparser.add_parser("batch", help="批量下载")
    batch_parser.add_argument("urls", nargs="+", help="下载链接,用空格隔开")
    batch_parser.add_argument("-d", "--dir", help="下载目录")

    # 查看下载任务
    list_parser = subparser.add_parser("list", help="查看下载任务")
    list_parser.add_argument(
        "status",
        choices=["completed", "deleted", "downloading", "waiting"],
        default="waiting",
        nargs="?",
    )

    # 删除下载任务
    delete_parser = subparser.add_parser("delete", help="删除下载任务")
    delete_parser.add_argument(
        "status",
        choices=["completed", "deleted", "downloading", "waiting"],
        default="waiting",
    )
    delete_parser.add_argument("task_ids", type=int, nargs="*")
    delete_parser.add_argument(
        "-f", "--forever", action="store_true", help="是否永久删除"
    )

    # 继续下载未完成的下载任务
    subparser.add_parser("resume", help="继续下载未完成的任务")

    # 停止下载
    subparser.add_parser("stop",help="停止下载")

    args = parser.parse_args()
    if args.command is None:
        # 没指定令命令的情况下进入交互式环境
        e(parser)
    else:
        execute(args)
    # 释放资源
    _download_manager.close()
