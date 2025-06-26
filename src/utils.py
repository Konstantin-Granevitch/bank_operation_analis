from pprint import pprint

import numpy as np
import pandas as pd
from pandas import DataFrame

from config import BASE_PATH


def xlsx_reader(file_name: str) -> DataFrame:
    """функция чтения данных из таблицы xlsx"""

    result = pd.read_excel(f"{BASE_PATH}/data/{file_name}")

    # возвращение результата с заменой отсутствия значений в таблице "nan" на None
    return result.replace(np.nan, None)


if __name__ == "__main__":
    # print(xlsx_reader("operations.xlsx").head())
    pprint(xlsx_reader("operations.xlsx").to_dict("records"))
