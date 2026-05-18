from datetime import date
import sys
import inflect


def main():
    birthday = input("Date of Birth: ")

    try:
        birth_date = get_date(birthday)
    except ValueError:
        sys.exit("Invalid date")

    minutes = get_minutes(birth_date)
    print(minutes_to_words(minutes))


def get_date(birthday):
    try:
        return date.fromisoformat(birthday)
    except ValueError:
        raise ValueError


def get_minutes(birth_date):
    today = date.today()
    days_old = today - birth_date
    return days_old.days * 24 * 60


def minutes_to_words(minutes):
    engine = inflect.engine()
    words = engine.number_to_words(minutes, andword="")
    return words.capitalize() + " minutes"


if __name__ == "__main__":
    main()
