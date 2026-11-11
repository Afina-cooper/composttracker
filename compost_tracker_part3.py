# === Stage 3: Хранилище в памяти ===
# Project: CompostTracker
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class CompostPile:
    name: str
    volume: float
    moisture: float
    created: date
    id: Optional[str] = None
    layers: List[str] = field(default_factory=list)


class MemoryStore:
    def __init__(self):
        self._piles: dict[str, CompostPile] = {}

    def add(self, pile: CompostPile) -> CompostPile:
        if not pile.id:
            pile.id = self._next_id()
        self._piles[pile.id] = pile
        return pile

    def get(self, pile_id: str) -> Optional[CompostPile]:
        return self._piles.get(pile_id)

    def list(self) -> List[CompostPile]:
        return list(self._piles.values())

    def _next_id(self) -> str:
        existing = {int(pile_id) for pile_id in self._piles if pile_id.isdigit()}
        counter = 1
        while counter in existing:
            counter += 1
        return str(counter)


if __name__ == "__main__":
    store = MemoryStore()
    first = store.add(
        CompostPile(
            name="Дача",
            volume=0.5,
            moisture=55.0,
            created=date(2024, 4, 1),
        )
    )
    second = store.add(
        CompostPile(
            name="Город",
            volume=0.2,
            moisture=60.0,
            created=date(2024, 4, 5),
        )
    )
    print(first.id, second.id)
    print(store.get(first.id).name)
    print(store.get(second.id).name)
    print([p.name for p in store.list()])
