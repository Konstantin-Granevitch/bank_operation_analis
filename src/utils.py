import logging
from pprint import pprint

import numpy as np
import pandas as pd
from pandas import DataFrame

from config import BASE_PATH

# инициализация логгера в модуле
func_logger = logging.getLogger("func_logger")
func_logger.setLevel(logging.DEBUG)
file_func_handler = logging.FileHandler(f"{BASE_PATH}/logs/func_log.log", mode="a")
file_func_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_func_handler.setFormatter(file_func_formatter)
func_logger.addHandler(file_func_handler)


def xlsx_reader(file_name: str) -> DataFrame:
    """функция чтения данных из таблицы xlsx"""

    func_logger.info("обращение к функции - xlsx_reader")

    try:
        result = pd.read_excel(f"{BASE_PATH}/data/{file_name}")

        func_logger.info("вывод DataFrame функцией - xlsx_reader")

        # возвращение результата с заменой отсутствия значений в таблице "nan" на None
        return result.replace(np.nan, None)
    except ValueError as e:
        func_logger.error(f"{e} обработка данных функцией - xlsx_reader невозможна, проверьте файл {file_name}")


if __name__ == "__main__":
    # print(xlsx_reader("operations.xlsx").head())
    pprint(xlsx_reader("operations.xlsx").to_dict("records"))
