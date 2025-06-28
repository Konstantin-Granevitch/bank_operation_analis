import datetime
import json
import logging
import os

import requests
from dotenv import load_dotenv

from config import BASE_PATH

# инициализация логгера в модуле
func_logger = logging.getLogger("func_logger")
func_logger.setLevel(logging.DEBUG)
file_func_handler = logging.FileHandler(f"{BASE_PATH}/logs/func_log.log", mode="a")
file_func_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_func_handler.setFormatter(file_func_formatter)
func_logger.addHandler(file_func_handler)


def api_currency(user_settings: str = "user_settings.json") -> str:
    """функция возвращающая запрос API с курсом валют согласно файла пользовательской конфигурации"""

    func_logger.info("обращение к функции - api_currency")

    # получение пользовательских данных
    func_logger.info(f"сбор данных для функции - api_currency из файла - {user_settings}")

    with open(f"{BASE_PATH}/data/{user_settings}") as f:
        file = json.load(f)

    func_logger.info("подготовка данных и формирование url запроса функцией - api_currency")

    currency = file["user_currencies"]
    symbols = ",".join(currency)
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    url = f"https://api.apilayer.com/exchangerates_data/{date}?base=RUB&symbols={symbols}"

    # загрузка "dotenv" библиотеки для создания заголовка с API ключем
    load_dotenv()
    api_key = os.getenv("API_KEY_CURRENCY")
    headers = {"apikey": api_key}

    try:
        func_logger.info("вывод результатов функцией - api_currency")

        # получение курса валют согласно пользовательских данных
        curse = requests.get(url, headers)

        return curse.json()
    except requests.exceptions.ConnectionError as e:
        func_logger.error(f"{e} вывод результатов api_currency - невозможен, проверьте соединение")


def api_stocks(user_settings: str = "user_settings.json") -> str:
    """функция возвращающая запрос API с курсом акций согласно файла пользовательской конфигурации"""

    func_logger.info("обращение к функции - api_stocks")

    # получение пользовательских данных
    func_logger.info(f"сбор данных для функции - api_stocks из файла - {user_settings}")

    with open(f"{BASE_PATH}/data/{user_settings}") as f:
        file = json.load(f)

    func_logger.info("подготовка данных и формирование url запроса функцией - api_stocks")

    stocks = file["user_stocks"]
    symbols = ",".join(stocks)
    url = f"https://financialmodelingprep.com/api/v3/quote/{symbols}?"

    # загрузка "dotenv" библиотеки для создания заголовка с API ключем
    load_dotenv()
    api_key = os.getenv("API_KEY_STOCKS")
    headers = {"apikey": api_key}

    try:
        func_logger.info("вывод результатов функцией - api_stocks")

        # получение курса акций согласно пользовательских данных
        stocks_api = requests.get(url, headers)

        return stocks_api.json()
    except requests.exceptions.ConnectionError as e:
        func_logger.error(f"{e} вывод результатов api_stocks - невозможен, проверьте соединение")


if __name__ == "__main__":
    print(api_currency())
    print(api_stocks())
