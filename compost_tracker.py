# === Stage 1: Каркас модуля ===
# Project: CompostTracker
from dataclasses import dataclass
from datetime import date


@dataclass
class CompostPile:
    name: str
    volume: float
    moisture: float
    start_date: date


def sample_piles() -> list[CompostPile]:
    return [
        CompostPile("Грядка северная", 1.5, 55.0, date(2024, 4, 12)),
        CompostPile("Куча у забора", 0.8, 60.0, date(2024, 5, 3)),
    ]


def main() -> None:
    piles = sample_piles()
    for pile in piles:
        print(f"Куча: {pile.name}")
        print(f"  Объём: {pile.volume:.2f} м³")
        print(f"  Влажность: {pile.moisture:.1f}%")
        print(f"  Дата закладки: {pile.start_date}")
        print()


if __name__ == "__main__":
    main()
