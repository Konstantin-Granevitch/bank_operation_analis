import datetime

current_date = datetime.datetime.now()


def main(date: str) -> list[dict]:
    """основная логика работы программы"""

    if 0 < date.hour < 6:
        print("Доброй ночи")
    elif 6 < date.hour < 12:
        print("Доброе утро")
    elif 12 < date.hour < 18:
        print("Добрый день")
    else:
        print("Добрый вечер")


if __name__ == "__main__":
    main(current_date)
