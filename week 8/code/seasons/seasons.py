import re 
import sys
from datetime import date
from inflect import engine

class HumanLiveTime:
    def __init__(self):
        pass  

    def calculate(self, birth_date: date) -> str:
        total_minutes = self._get_total_minutes(birth_date)
        return self._minutes_to_words(total_minutes)

    def _get_total_minutes(self, birth_date: date) -> int:
        today = date.today()
        delta = today - birth_date
        return int(delta.total_seconds() // 60) 

    def _minutes_to_words(self, minutes: int) -> str:
        e = engine()
        words = e.number_to_words(minutes, andword="")  
        return f"{words.capitalize()} minutes"


def main():
    birth_str = input("Date of Birth: ").strip()
    birth_date = is_valid_birth_date(birth_str)

    if not birth_date:
        sys.exit("Invalid date")

    human = HumanLiveTime()
    print(human.calculate(birth_date))


def is_valid_birth_date(birth_str: str):

    if re.match(r"^\d{4}-\d{2}-\d{2}$", birth_str):
        try:
            return date.fromisoformat(birth_str)
        except ValueError:
            return False
    return False


if __name__ == "__main__":
    main()
