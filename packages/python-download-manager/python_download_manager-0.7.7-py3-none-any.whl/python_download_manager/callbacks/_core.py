from .. import _unpack
from .._database import DownloadingTask
from .._serialization import serializable
from .._typehint import StrPath


@serializable
class Callback:

    # @abstractmethod
    def __call__(self, task: DownloadingTask):
        raise NotImplementedError

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"{self.__class__.__name__}{self.__dict__}"


class UnpackArchive(Callback):
    def __init__(
            self,
            unpack_dir: StrPath = None,
            password: str = None,
            delete_later: bool = False,
            missing_ok: bool = False,
            extra_ext: list = None,
    ):
        self.unpack_dir = unpack_dir
        self.password = password
        self.delete_later = delete_later
        self.missing_ok = missing_ok
        if extra_ext is None:
            self.extra_ext = []
        else:
            self.extra_ext = [ext.lower() for ext in extra_ext]

    def __call__(self, task: DownloadingTask):
        # archive path
        archive_path = task.file_path
        # ext
        default_ext = (
            # rarfile ext
            ".rar",
            ".cbr",
            # 7zfile ext
            ".7z",
            ".cb7",
            # zipfile ext
            ".zip",
            ".cbz",
        )
        if (
                archive_path.suffix not in default_ext
                and archive_path.suffix not in self.extra_ext
        ):
            return
        # if archive file not exist
        if not archive_path.exists():
            if self.missing_ok:
                return
            else:
                raise FileExistsError(f"Archive file does't exist:{archive_path}")
        # unpack dir
        unpack_dir = self.unpack_dir or archive_path.with_name(archive_path.stem)
        unpack_dir.mkdir(parents=True, exist_ok=True)
        # unpack
        _unpack.unpack_archive(archive_path, unpack_dir, self.password)
        # delte
        if self.delete_later:
            self.archive_path.unlink(missing_ok=True)
