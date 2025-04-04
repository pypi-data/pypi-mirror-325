import base64
import importlib
import json
from datetime import date, datetime
from pathlib import Path, PurePath


class PDMJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return {
                "__type__": "bytes",
                "base64": base64.b64encode(obj).decode("utf-8"),
            }
        elif hasattr(obj, "___serializable"):
            dumped_data = {
                "module": obj.__module__,
                "class": obj.__class__.__name__,
                "args": getattr(obj, "___args"),
                "kwargs": getattr(obj, "___kwargs"),
            }
            return {"__type__": "Serializble", "dumped_data": dumped_data}
        elif isinstance(obj, date):
            return {"__type__": "date", "iso": obj.isoformat()}
        elif isinstance(obj, PurePath):
            return {"__type__": "Path", "path": str(obj)}
        elif isinstance(obj, set):
            return {"__type__": "set", "values": list(obj)}
        return super().default(obj)


class PDMJsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if "__type__" not in obj:
            return obj
        type_ = obj["__type__"]
        if type_ == "bytes":
            return base64.b64decode(obj["base64"].encode("utf-8"))
        elif type_ == "Serializble":
            dumped_data = obj["dumped_data"]
            module = importlib.import_module(dumped_data["module"])
            callback_class = getattr(module, dumped_data["class"])
            return callback_class(*dumped_data["args"], **dumped_data["kwargs"])
        elif type_ == "date":
            return datetime.fromisoformat(obj["iso"])
        elif type_ == "Path":
            return Path(obj["path"])
        elif type_ == "set":
            return set(obj["values"])
        return obj
