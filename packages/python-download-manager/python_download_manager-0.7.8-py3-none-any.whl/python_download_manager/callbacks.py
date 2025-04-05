from pathlib import Path
from typing import Optional, Union

import patoolib


class Callback:
    pass


class UnpackArchive(Callback):
    def __init__(
            self,
            archive_path: Union[str, Path],
            outdir: Union[str, Path] = None,
            password: Optional[str] = None,
            delete_file_after_unpack: bool = False,
            missing_ok=False
    ):
        self.archive_path = Path(archive_path)
        if outdir:
            self.outdir = outdir
        else:
            self.outdir = self.archive_path.parent
        self.password = password
        self.delete_file_after_unpack = delete_file_after_unpack
        self.missing_ok = missing_ok

    def __call__(self):
        if not self.archive_path.exists() and self.missing_ok:
            return
        patoolib.extract_archive(str(self.archive_path), outdir=str(self.outdir), password=self.password)
        if self.delete_file_after_unpack:
            self.archive_path.unlink(missing_ok=True)
