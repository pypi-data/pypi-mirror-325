from abc import ABC, abstractmethod

from tqdm import tqdm


class ProgressAdapter(ABC):

    def __init__(
            self, total: int, *, initial: int = 0, desc: str = None, info: dict = None
    ):
        pass

    # region methods

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def update(self, increment: int = 1):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def write_message(message, file=None, end="\n"):
        raise NotImplementedError

    # endregion

    # region properties
    @property
    @abstractmethod
    def desc(self):
        raise NotImplementedError

    @desc.setter
    @abstractmethod
    def desc(self, desc: str):
        raise NotImplementedError

    @property
    @abstractmethod
    def info(self):
        raise NotImplementedError

    @info.setter
    @abstractmethod
    def info(self, info: dict):
        raise NotImplementedError

    @property
    @abstractmethod
    def pos(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def progress(self) -> int:
        raise NotImplementedError

    @progress.setter
    @abstractmethod
    def progress(self, n):
        raise NotImplementedError

    @property
    @abstractmethod
    def total(self):
        raise NotImplementedError

    @total.setter
    @abstractmethod
    def total(self):
        raise NotImplementedError

    # endregion

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.close()
        return False


class TqdmAdapter(ProgressAdapter):

    def __init__(
            self, total: int, *, initial: int = 0, desc=None, info=None, position=None
    ):
        super().__init__(total, initial=initial, desc=desc, info=info)
        self._bar = tqdm(
            desc=desc,
            total=total,
            initial=initial,
            unit="B",
            unit_scale=True,
            unit_divisor=1024,
            postfix=info or {},
            position=position
        )

    # region methods
    def close(self):
        self._bar.set_description("done")
        self._bar.close()

    def reset(self):
        self._bar.reset()

    def update(self, increment: int = 1):
        self._bar.update(increment)

    @staticmethod
    def write_message(message: str, file=None, end="\n"):
        tqdm.write(message, file, end)

    # endregion

    # region properties
    @property
    def desc(self):
        return self._bar.desc

    @desc.setter
    def desc(self, desc: str):
        self._bar.set_description(desc)

    @property
    def info(self):
        return self._bar.postfix

    @info.setter
    def info(self, info: dict):
        self._bar.set_postfix(info)
        self._bar.refresh()

    @property
    def pos(self) -> int:
        return self._bar.pos

    @property
    def progress(self) -> int:
        return self._bar.n

    @progress.setter
    def progress(self, n):
        self._bar.n = n
        self._bar.refresh()

    @property
    def total(self):
        return self._bar.total

    @total.setter
    def total(self, total: int):
        self._bar.total = total
        self._bar.refresh()

    # endregion
