# === Stage 4: Редактирование записей ===
# Project: CompostTracker
ALLOWED_FIELDS = {"название", "объём", "влажность", "дата закладки"}

VALID_UNITS = {
    "название": str,
    "объём": (int, float),
    "влажность": (int, float),
    "дата закладки": str,
}

MAX_VOLUME = 1000.0
MAX_MOISTURE = 100.0
MIN_MOISTURE = 0.0


class CompostPileError(Exception):
    pass


def is_valid_update(payload):
    if not isinstance(payload, dict):
        return False

    changed = set(payload.keys())

    if changed - ALLOWED_FIELDS:
        return False

    for field, value in payload.items():
        if field not in VALID_UNITS:
            continue
        expected = VALID_UNITS[field]
        if isinstance(expected, tuple):
            if not isinstance(value, expected):
                return False
        else:
            if not isinstance(value, expected):
                return False
    return True


def clamp_volume(value):
    return max(0.0, min(value, MAX_VOLUME))


def clamp_moisture(value):
    return max(MIN_MOISTURE, min(value, MAX_MOISTURE))


def normalize_value(field, value):
    if field == "название":
        return value.strip()
    if field == "объём":
        return clamp_volume(float(value))
    if field == "влажность":
        return clamp_moisture(float(value))
    return value


def update_pile(pile, payload):
    if not is_valid_update(payload):
        raise CompostPileError("Недопустимые поля для обновления")

    for field, value in payload.items():
        pile[field] = normalize_value(field, value)

    return pile
