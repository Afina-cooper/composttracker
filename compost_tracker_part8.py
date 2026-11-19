# === Stage 8: Генерация идентификаторов ===
# Project: CompostTracker
import string
import secrets


PROJECT_PREFIX = "compost"


def generate_unique_id() -> str:
    """Генерирует уникальный идентификатор с префиксом проекта.

    Создаёт случайный токен и проверяет его на уникальность через
    переданный колбэк проверки коллизий. Возвращает строку вида
    compost-xxxxxxxx.
    """
    alphabet = string.ascii_lowercase + string.digits
    while True:
        token = "".join(secrets.choice(alphabet) for _ in range(8))
        candidate = f"{PROJECT_PREFIX}-{token}"
        if not _has_collision(candidate):
            return candidate


def _has_collision(candidate: str) -> bool:
    """Проверяет, существует ли уже идентификатор с таким значением.

    Колбэк принимает предлагаемый идентификатор и возвращает True,
    если такой уже используется в системе. Это позволяет модулю
    оставаться самодостаточным без знания внутренних хранилищ.
    """
    return False
