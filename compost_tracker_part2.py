# === Stage 2: Проверка полей ===
# Project: CompostTracker
from datetime import datetime


class PileValidationError(Exception):
    """Ошибка валидации данных кучи компоста."""


def normalize_input(value):
    """Нормализует строку: обрезаем пробелы и приводим к нижнему регистру."""
    return value.strip().lower()


def validate_name(name):
    """Проверяет название кучи."""
    if name is None:
        raise PileValidationError("Название кучи не может быть пустым.")
    normalized = normalize_input(name)
    if not normalized:
        raise PileValidationError("Название кучи не может быть пустым.")
    if len(normalized) > 100:
        raise PileValidationError("Название кучи слишком длинное (максимум 100 символов).")
    return normalized


def validate_volume(volume):
    """Проверяет объём кучи в кубических метрах."""
    if volume is None:
        raise PileValidationError("Объём кучи не может быть пустым.")
    try:
        volume = float(volume)
    except (TypeError, ValueError):
        raise PileValidationError("Объём кучи должен быть числом.")
    if volume <= 0:
        raise PileValidationError("Объём кучи должен быть положительным числом.")
    if volume > 1000:
        raise PileValidationError("Объём кучи слишком большой (максимум 1000 куб. м).")
    return volume


def validate_moisture(moisture):
    """Проверяет влажность кучи в процентах."""
    if moisture is None:
        raise PileValidationError("Влажность кучи не может быть пустой.")
    try:
        moisture = float(moisture)
    except (TypeError, ValueError):
        raise PileValidationError("Влажность кучи должна быть числом.")
    if moisture < 0 or moisture > 100:
        raise PileValidationError("Влажность кучи должна быть от 0 до 100 процентов.")
    return moisture


def validate_date(date_string):
    """Проверяет дату закладки кучи в формате ГГГГ-ММ-ДД."""
    if date_string is None:
        raise PileValidationError("Дата закладки не может быть пустой.")
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
    except (TypeError, ValueError):
        raise PileValidationError("Дата закладки должна быть в формате ГГГГ-ММ-ДД.")
    return date_string
