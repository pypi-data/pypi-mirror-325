from abc import ABC, abstractmethod

from tqdm import tqdm


class ProgressAdapter(ABC):

    def __init__(self, total: int, info: dict = None):
        self.total = total
        self.info = info or {}

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def pos(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def set_info(self, info: dict):
        raise NotImplementedError

    @abstractmethod
    def update(self, increase: int = 1):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def write_message(message, file=None, end="\n"):
        raise NotImplementedError

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.close()
        return False


class TqdmAdapter(ProgressAdapter):

    def __init__(self, total: int, info=None):
        super().__init__(total, info)
        self._bar = tqdm(
            desc="downloading",
            total=total,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            postfix=info or {}
        )

    def close(self):
        self._bar.set_description("done")
        self._bar.close()

    @property
    def pos(self) -> int:
        return self._bar.pos

    def reset(self):
        self._bar.set_description("downloading")
        self._bar.reset()

    def update(self, increase: int = 1):
        self._bar.update(increase)

    def set_info(self, info: dict):
        self._bar.set_postfix(info)

    @staticmethod
    def write_message(message: str, file=None, end="\n"):
        tqdm.write(message, file, end)
