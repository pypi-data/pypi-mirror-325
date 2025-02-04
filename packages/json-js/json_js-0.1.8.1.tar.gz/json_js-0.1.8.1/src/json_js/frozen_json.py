from typing import Any, Mapping, override

from .json import JSON

class FrozenJSON(JSON):
    def __init__(self, data: Mapping[Any, Any]) -> None:
        super().__init__(data)

    @override
    def __repr__(self) -> str:
        return f"<FrozenJSON({self._JSON__data!r}>)"
