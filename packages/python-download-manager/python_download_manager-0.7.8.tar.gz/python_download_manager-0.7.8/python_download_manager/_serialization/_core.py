import json
from typing import Any, Union

from ._coder import PDMJsonDecoder, PDMJsonEncoder


def dumps(obj: "serializable") -> str:
    return json.dumps(obj, cls=PDMJsonEncoder)


def loads(s: Union[str, bytes]) -> Any:
    return json.loads(s, cls=PDMJsonDecoder)
