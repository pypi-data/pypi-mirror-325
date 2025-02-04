from typing import Any, MutableMapping

from .json import JSON

class MutableJSON(JSON):
    def __init__(self, data: MutableMapping[Any, Any]) -> None:
        raise NotImplemented
        super().__init__(data)

    def __setattr__(self, key, value: Any) -> None:
        pass

    def __repr__(self) -> str:
        return f"<MutableJSON({self._JSON__data!r}>)"
