import functools


def serializable(cls):
    @functools.wraps(cls.__new__)
    def wrapped__new__(cls, *args, **kwargs):
        obj = cls.___origin__new(cls)
        obj.___args = args
        obj.___kwargs = kwargs
        return obj

    cls.___serializable = True
    cls.___origin__new = cls.__new__
    cls.__new__ = wrapped__new__
    return cls
