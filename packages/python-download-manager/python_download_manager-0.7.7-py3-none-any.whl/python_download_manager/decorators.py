import functools


def synchronized(lock):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                return func(*args, **kwargs)

        return wrapper

    return decorator


def classproperty(func):
    class ClassPropertyDescriptor:
        def __init__(self, fget):
            self.fget = fget

        def __get__(self, instance, owner):
            return self.fget(owner)

    return ClassPropertyDescriptor(func)
