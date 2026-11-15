# === Stage 5: Удаление и восстановление ===
# Project: CompostTracker
from datetime import datetime


class SoftDeleteMixin:
    def __init__(self, *, is_deleted=False):
        self.is_deleted = is_deleted

    def delete(self):
        self.is_deleted = True

    def restore(self):
        self.is_deleted = False

    @property
    def is_active(self):
        return not self.is_deleted


class CompostPile(SoftDeleteMixin):
    def __init__(self, name, volume, moisture, created_date):
        super().__init__()
        self.name = name
        self.volume = volume
        self.moisture = moisture
        self.created_date = created_date

    def to_dict(self):
        return {
            "name": self.name,
            "volume": self.volume,
            "moisture": self.moisture,
            "created_date": self.created_date,
            "is_deleted": self.is_deleted,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            volume=data["volume"],
            moisture=data["moisture"],
            created_date=data["created_date"],
            is_deleted=data.get("is_deleted", False),
        )
