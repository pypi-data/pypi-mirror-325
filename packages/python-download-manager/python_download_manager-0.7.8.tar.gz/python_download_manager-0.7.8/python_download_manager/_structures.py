import threading

class ThreadSafeDict(dict):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._lock = threading.Lock()

    def __setitem__(self, key, value):
        with self._lock:
            super().__setitem__(key,value)

    def __delitem__(self, key):
        with self._lock:
            super().__delitem__(key)
