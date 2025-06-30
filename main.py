import datetime
import os
from pprint import pprint
from typing import Any

from config import BASE_PATH
from src.utils import xlsx_reader
from src.views import api_currency, api_stocks

current_date = datetime.datetime.now()


def main(date: str) -> Any:
    """основная логика работы программы"""

    # приветствие пользователя с привязкой ко времени суток
    if 0 < date.hour < 6:
        print("Доброй ночи\n")
    elif 6 < date.hour < 12:
        print("Доброе утро\n")
    elif 12 < date.hour < 18:
        print("Добрый день\n")
    else:
        print("Добрый вечер\n")

    # запрос у пользователя файла с транзакциями и проверка на корректный ввод имени файла
    while True:
        file_name = input(
            "Закиньте файл с транзакциями в проект в папку 'data' и введите его полное имя 'file.xlsx'\n"
        )
        if not (os.path.exists(f"{BASE_PATH}/data/{file_name}")):
            print("Ваш файл не найден, проверьте правильность и попробуйте снова")
            continue
        else:
            break

    list_transactions = xlsx_reader(file_name).to_dict("records")

    # создание списка словарей со всеми картами участвовавших в транзакциях с подсчетом сумм операций и кешбэка
    card_cost = {}

    for transaction in list_transactions:
        if transaction["Номер карты"] is None:
            continue
        elif transaction["Номер карты"] in card_cost.keys():
            card_cost[transaction["Номер карты"]] += transaction["Сумма платежа"]
        else:
            card_cost[transaction["Номер карты"]] = transaction["Сумма платежа"]

    cards_info = []
    n = 0

    for key, value in card_cost.items():
        info = {}
        info["Номер карты"] = key
        info["Сумма операций"] = round(value, 2)

        if value < 0:
            info["Кешбэк"] = abs(round(value / 100, 2))
        else:
            info["Кешбэк"] = 0

        cards_info.append(info)
        n += 1
    # создание отсортированного списка транзакций для поиска топ 5 по сумме
    top_transactions = sorted(list_transactions, key=lambda trans: trans["Сумма операции с округлением"], reverse=True)
    print("Топ 5 транзакций по сумме операции")
    pprint(top_transactions[:4])

    # распечатка текущих курсов валюты и акций согласно списка из файла пользователя user_settings.json
    print("По каждой карте: сумма операции и кешбэк")
    pprint(cards_info)
    print("--------------------------------------------------------")
    print("Топ 5 транзакций по сумме операции")
    pprint(top_transactions[:4])
    print("--------------------------------------------------------")
    print("Текущий курс валют")
    pprint(api_currency())
    print("--------------------------------------------------------")
    print("Текущий курс акций")
    pprint(api_stocks())


if __name__ == "__main__":
    main(current_date)
