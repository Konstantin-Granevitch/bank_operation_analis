import json
import logging
import re
from pprint import pprint

from config import BASE_PATH
from src.utils import xlsx_reader

# инициализация логгера в модуле
func_logger = logging.getLogger("func_logger")
func_logger.setLevel(logging.DEBUG)
file_func_handler = logging.FileHandler(f"{BASE_PATH}/logs/func_log.log", mode="a")
file_func_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_func_handler.setFormatter(file_func_formatter)
func_logger.addHandler(file_func_handler)


def finder(list_transactions: list[dict], attribute: str) -> str:
    """функция поиска транзакций по условию в виде строки"""

    func_logger.info("обращение к функции - finder")

    result = []

    for transaction in list_transactions:
        if attribute in str(transaction):
            result.append(transaction)

    if result == []:
        func_logger.info(f"функция - finder успешно отработала")

        return "искомые транзакции отсутствуют"
    else:
        func_logger.info(f"функция - finder успешно отработала")

        return json.dumps(result, ensure_ascii=False)


def tel_finder(list_transactions: list[dict]) -> str:
    """Функция поиска транзакций в описании которых присутствуют телефонные номера"""

    func_logger.info("обращение к функции - tel_finder")

    tel_number = re.compile(r"[+]\d\s\d{3}.\d{2}.\d{2}")
    result = []

    for transaction in list_transactions:
        if re.search(tel_number, str(transaction)):
            result.append(transaction)

    if result == []:
        func_logger.info("функция - tel_finder успешно отработала")

        return "транзакции с телефонными номерами отсутствуют"
    else:
        func_logger.info("функция - tel_finder успешно отработала")

        return json.dumps(result, ensure_ascii=False)


if __name__ == "__main__":
    transactions = xlsx_reader("operations.xlsx").to_dict("records")
    pprint(json.loads(finder(transactions, "*5091")))
