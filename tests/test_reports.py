import os
import pandas as pd

from src.reports import report_to_file, category_cost


# @report_to_file("test_file.json")
# def test_func(x: int, y: int) -> int:
#     return x + y
# test_func(3, 2)
#
# def test_report_to_file():
#     test_func(3, 2)
#
#     with open("test_file.json") as f:
#         test_data = int(f.read())
#
#     assert test_data == 5
#     os.remove("test_file.json")


def test_category_cost(list_transactions):
    result = category_cost(pd.DataFrame(list_transactions), "Супермаркеты", "05.01.2018")

    assert result == f"По категории - Супермаркеты в указанном периоде потрачено: 73.06 руб"