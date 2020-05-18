import datetime
from typing import Dict, Union

from .dosage import Dosage, dosages


class Model():
    def __init__(
        self,
        start: str,
        from_last: float,
        total: int,
        dosages: dosages,
    ):

        self.start: datetime.datetime = datetime.datetime.fromisoformat(start)
        self.from_last = from_last
        self.total = total
        self.dosage = Dosage(dosages)

        now = datetime.datetime.now()
        per_day = self.dosage.per_day
        first_day_taken = self.dosage.will_take(self.start.time())
        taken = (now - self.start).days * per_day \
            + self.dosage.taken(now.time()) + first_day_taken
        can_cover = self.total + self.from_last
        if taken >= can_cover:
            even = int((taken - first_day_taken - self.from_last) / self.total \
                * self.total + self.from_last)
            days = int(even / per_day + 1 if first_day_taken else even / per_day)
            time, left = self.dosage.time_and_left(even % per_day)
            self.from_last = left
            self.start += datetime.timedelta(days=days - 1)
            self.start.replace(hour=time.hour, minute=time.minute, second=time.second)

    def check(self, num: float) -> bool:
        if num < 0.0:
            num = self.total + num
        now = datetime.datetime.now()
        if num == self.total + self.from_last - self.dosage.will_take(self.start.time()) \
            - self.dosage.taken(now.time()) - ((now - self.start).days * self.dosage.per_day):
            return True
        else:
            return False

    def to_dict(self) -> Dict[str, Union[str, int, float, dosages]]:
        return {
            'start': self.start.isoformat(),
            'from_last': self.from_last,
            'total': self.total,
            'dosages': self.dosage.to_dict()
        }
