import os

import pandas as pd

from config import BASE_PATH
from src.reports import category_cost, report_to_file


@report_to_file("test_file.json")
def func(x: int, y: int) -> int:
    """тестовая функция для проверки декоратора"""
    return x + y


def test_report_to_file():
    func(3, 2)

    with open(f"{BASE_PATH}/data/test_file.json") as f:
        test_data = int(f.read())

    assert test_data == 5
    os.remove(f"{BASE_PATH}/data/test_file.json")


def test_category_cost(list_transactions):
    # тест на наличие операций с потраченными средствами
    result = category_cost(pd.DataFrame(list_transactions), "Супермаркеты", "05.01.2018")

    assert result == "По категории - Супермаркеты в указанном периоде потрачено: 73.06 руб"

    # тест на отсутствие операций
    result_none = category_cost(pd.DataFrame(list_transactions), "kjdfkgjbnk", "05.01.2018")

    assert result_none == "По категории - kjdfkgjbnk в указанный период трат не было"

    # тест на наличие операций с пополнением счета
    result_back = category_cost(pd.DataFrame(list_transactions), "Пополнения", "11.01.2018")

    assert result_back == "По категории - Пополнения в указанном периоде получено: 30000.0 руб"
