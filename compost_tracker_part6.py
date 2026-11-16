# === Stage 6: Связанная сущность ===
# Project: CompostTracker
from datetime import date


class Measurement:
    def __init__(self, heap_id, date, temperature):
        self.heap_id = heap_id
        self.date = date
        self.temperature = temperature

    def __repr__(self):
        return f"Measurement(heap_id={self.heap_id}, date={self.date}, temperature={self.temperature})"


def add_measurement(heap_id, date, temperature):
    return Measurement(heap_id, date, temperature)


def read_measurements(heap_id, measurements):
    return [m for m in measurements if m.heap_id == heap_id]


def average_temperature(measurements):
    if not measurements:
        return 0.0
    return sum(m.temperature for m in measurements) / len(measurements)


def is_ripe(measurements):
    if not measurements:
        return False
    temperatures = [m.temperature for m in measurements]
    return max(temperatures) < 30 and min(temperatures) > 20
