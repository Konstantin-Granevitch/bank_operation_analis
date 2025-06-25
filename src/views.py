import copy
import datetime
import json
import os
from pprint import pprint

import requests
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

from config import BASE_PATH
from src.utils import xlsx_reader


def api_currency(user_settings: str = "user_settings.json") -> str:
    """функция возвращающая запрос API с курсом валют согласно файла пользовательской конфигурации"""

    # получение пользовательских данных
    with open(f"{BASE_PATH}/data/{user_settings}") as f:
        file = json.load(f)

    currency = file["user_currencies"]
    symbols = ",".join(currency)
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    url = f"https://api.apilayer.com/exchangerates_data/{date}?base=RUB&symbols={symbols}"

    # загрузка "dotenv" библиотеки для создания заголовка с API ключем
    load_dotenv()
    api_key = os.getenv("API_KEY_CURRENCY")
    headers = {"apikey": api_key}

    # получение курса валют согласно пользовательских данных
    curse = requests.get(url, headers)

    return curse.json()


def api_stoks(user_settings: str = "user_settings.json") -> str:
    """функция возвращающая запрос API с курсом акций согласно файла пользовательской конфигурации"""

    # получение пользовательских данных
    with open(f"{BASE_PATH}/data/{user_settings}") as f:
        file = json.load(f)

    stoks = file["user_stocks"]
    symbols = ",".join(stoks)
    url = f"https://financialmodelingprep.com/api/v3/quote/{symbols}?"

    # загрузка "dotenv" библиотеки для создания заголовка с API ключем
    load_dotenv()
    api_key = os.getenv("API_KEY_STOKS")
    headers = {"apikey": api_key}

    # получение курса акций согласно пользовательских данных
    stoks = requests.get(url, headers)

    return stoks.json()


def main_views(user_date: str, interval: str = "M") -> str:
    """
    функция показывает расходы/доходы, курс валют и стоимость акций в указанный промежуток времени
    """

    date_gr1 = datetime.datetime.strptime(user_date, "%d.%m.%Y")
    if interval == "M":
        date_gr2 = date_gr1 - relativedelta(months=1)
    elif interval == "W":
        date_gr2 = date_gr1 - relativedelta(weeks=1)
    elif interval == "Y":
        date_gr2 = date_gr1 - relativedelta(years=1)
    else:
        date_gr2 = None

    if date_gr2 is None:
        lst_trans_date = copy.copy(list_transactions)
    else:
        lst_trans_date = []

        for trans in list_transactions:
            lst_trans = trans["Дата операции"].split(" ")
            date_trans = datetime.datetime.strptime(lst_trans[0], "%d.%m.%Y")
            if date_gr2 < date_trans < date_gr1:
                lst_trans_date.append(trans)
    pass


if __name__ == "__main__":
    # list_transactions = xlsx_reader("operations.xlsx").to_dict('records')
    # pprint(main_views("01.01.2018"))
    # print(api_currency("user_settings.json"))
    pprint(api_stoks("user_settings.json"))
