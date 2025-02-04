import keyword
from typing import Any, Mapping, Sequence, KeysView


class JSON:
    def __new__(cls, obj) -> Any:
        if isinstance(obj, Mapping):
            return super().__new__(cls)
        elif isinstance(obj, Sequence):
            return [cls(item) for item in obj]
        else:
            return obj

    def __init__(self, data: Mapping[str, Any]) -> None:
        self.__data = {}
        for key, value in data.items():
            if keyword.iskeyword(key):
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name) -> Any:
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return self.__class__(self.__data[name])

    def __dir__(self) -> KeysView[Any]:
        return self.__data.keys()

    def __repr__(self) -> str:
        return f"<JSON({self.__data!r}>)"
