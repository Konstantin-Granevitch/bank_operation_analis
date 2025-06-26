import datetime
import json
import os

import requests
from dotenv import load_dotenv

from config import BASE_PATH


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
