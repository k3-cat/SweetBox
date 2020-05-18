import datetime
from typing import Dict, Union

dosages = Dict[str, float]


class Dosage():
    def __init__(self, dosages: dosages):
        self.dosages = dict()
        self.per_day = 0.0
        for time, amount in dosages.items():
            self.dosages[datetime.time.fromisoformat(time)] = amount
            self.per_day += amount

    def taken(self, time_: datetime.time) -> float:
        taken = 0.0
        for time, amount in self.dosages.items():
            if time_ <= time:
                return taken
            taken += amount

    def will_take(self, time_) -> float:
        return self.per_day - self.taken(time_)

    def time_and_left(self, left: float) -> Union[datetime.time, float]:
        for time, amount in self.dosages.items():
            left -= amount
            if left > 0.0:
                continue
            if left < 0.0:
                left += amount
            return time, left

    def to_dict(self) -> dosages:
        return {time.isoformat(): amount for time, amount in self.dosages.items()}
