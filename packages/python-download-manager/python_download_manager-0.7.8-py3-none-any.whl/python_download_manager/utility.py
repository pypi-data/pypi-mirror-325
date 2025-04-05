import math
from pathlib import Path
from urllib import parse

from .database import Chunk


def get_filename_from_url(url: str):
    """
    概述：从给定的URL中提取文件名。

    参数：一个字符串类型的URL。

    返回值：提取出的文件名，类型为字符串。
    """
    parse_result = parse.urlparse(url)
    if parse_result.path == "":
        filename = parse_result.netloc
    else:
        filename = Path(parse_result.path).name
    return filename


def slice_file(file_size: int, chunk_size: int) -> list[Chunk]:
    """
    概述：该函数用于将一个给定大小的文件分割成多个指定大小的块。

    参数：
        file_size (int)：文件的总大小。
        chunk_size (int)：每个块的大小。

    返回值： 返回一个包含多个 Chunk 对象的列表，每个 Chunk 对象表示一个文件块，包含该块的起始位置 (start) 和结束位置 (end)。
    如果 file_size 为 -1，则返回一个包含单个 Chunk 对象的列表，其 start 和 end 均为 -1 和 -2。
    """
    if file_size == -1:
        return [Chunk(start=-1, end=-2)]
    chunk_count = math.ceil(file_size / chunk_size)
    chunks = []
    for chunk_index in range(chunk_count):
        chunk = Chunk(
            start=chunk_index * chunk_size,
            end=min((chunk_index + 1) * chunk_size, file_size) - 1,
        )
        chunks.append(chunk)
    return chunks


def format_file_size(size: int) -> str:
    """
    概述：该函数用于将文件大小格式化为易读的字符串表示。

    参数：size（int）：文件大小，以字节为单位。

    返回值：str：格式化后的文件大小字符串，包含适当的单位（如 B、KB、MB 等）。
    """
    units = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    for unit in units:
        if size < 1024:
            return f"{size} {unit}"
        size /= 1024
