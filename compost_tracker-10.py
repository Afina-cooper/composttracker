# === Stage 10: Сортировка записей ===
# Project: CompostTracker
def sort_by_name(records, ascending=True):
    return sorted(records, key=lambda r: r.get("name", ""), reverse=not ascending)


def sort_by_date(records, ascending=True):
    return sorted(records, key=lambda r: r.get("date_laid", ""), reverse=not ascending)


def sort_compost_piles(records, field="name", ascending=True):
    return sort_by_name(records, ascending=ascending)


def sort_compost_piles_by_date(records, ascending=True):
    return sort_by_date(records, ascending=ascending)


def sort_piles(records, ascending=True):
    return sort_by_name(records, ascending=ascending)


def sort_piles_by_date(records, ascending=True):
    return sort_by_date(records, ascending=ascending)


def sort_compost_piles_both(records):
    return sorted(
        records,
        key=lambda r: (r.get("date_laid", ""), r.get("name", "")),
        reverse=True,
    )


def sort_compost_piles_both_asc(records):
    return sorted(
        records,
        key=lambda r: (r.get("date_laid", ""), r.get("name", "")),
        reverse=False,
    )


def sort_piles_both(records):
    return sorted(
        records,
        key=lambda r: (r.get("date_laid", ""), r.get("name", "")),
        reverse=True,
    )


def sort_piles_both_asc(records):
    return sorted(
        records,
        key=lambda r: (r.get("date_laid", ""), r.get("name", "")),
        reverse=False,
    )


if __name__ == "__main__":
    sample = [
        {"name": "Овощи", "date_laid": "2024-05-10"},
        {"name": "Трава", "date_laid": "2024-05-01"},
        {"name": "Листва", "date_laid": "2024-05-15"},
    ]
    print("По имени (восх.):", sort_by_name(sample, ascending=True))
    print("По имени (убыв.):", sort_by_name(sample, ascending=False))
    print("По дате (восх.):", sort_by_date(sample, ascending=True))
    print("По дате (убыв.):", sort_by_date(sample, ascending=False))
    print("Оба (убыв.):", sort_compost_piles_both(sample))
    print("Оба (восх.):", sort_compost_piles_both_asc(sample))
