from typing import Any, Dict, Optional


class DataStorage:
    def __init__(self) -> None:
        self.storage: Dict[str, Any] = {}

    def create(self, key: str, value: Any) -> None:
        self.storage[key] = value

    def read(self, key: str) -> Optional[Any]:
        return self.storage.get(key)

    def update(self, key: str, value: Any) -> None:
        if key in self.storage:
            self.storage[key] = value

    def delete(self, key: str) -> None:
        if key in self.storage:
            del self.storage[key]
