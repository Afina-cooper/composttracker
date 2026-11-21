# === Stage 9: Фильтрация записей ===
# Project: CompostTracker
from datetime import date


def filter_by_volume(records, min_volume=None, max_volume=None):
    filtered = []
    for record in records:
        volume = record.get("объём")
        if min_volume is not None and volume < min_volume:
            continue
        if max_volume is not None and volume > max_volume:
            continue
        filtered.append(record)
    return filtered


def filter_by_date_range(records, start_date=None, end_date=None):
    filtered = []
    for record in records:
        record_date = record.get("дата закладки")
        if isinstance(record_date, str):
            record_date = date.fromisoformat(record_date)
        if start_date is not None and record_date < start_date:
            continue
        if end_date is not None and record_date > end_date:
            continue
        filtered.append(record)
    return filtered


def filter_compost_piles(records, min_volume=None, max_volume=None,
                         start_date=None, end_date=None):
    filtered = records
    filtered = filter_by_volume(filtered, min_volume, max_volume)
    filtered = filter_by_date_range(filtered, start_date, end_date)
    return filtered
