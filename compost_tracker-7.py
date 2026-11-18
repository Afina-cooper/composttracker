# === Stage 7: Связи между сущностями ===
# Project: CompostTracker
from datetime import datetime


class CompostPile:
    def __init__(self, name, volume, moisture, laid_out_date):
        self.name = name
        self.volume = volume
        self.moisture = moisture
        self.laid_out_date = laid_out_date


class CompostReading:
    def __init__(self, timestamp, pile, temperature):
        self.timestamp = timestamp
        self.pile = pile
        self.temperature = temperature


def get_readings(pile, readings):
    return [reading for reading in readings if reading.pile is pile]


def get_readings_by_name(pile_name, readings):
    return [reading for reading in readings if reading.pile.name == pile_name]


def check_integrity(pile, readings):
    linked = get_readings(pile, readings)
    if linked:
        return linked
    if any(reading.pile.name == pile.name for reading in readings):
        return [reading for reading in readings if reading.pile.name == pile.name]
    return []


def get_readings_and_check(pile, readings):
    linked = get_readings(pile, readings)
    linked_by_name = get_readings_by_name(pile.name, readings)
    if linked and linked_by_name:
        return linked, linked_by_name
    return linked, linked_by_name
