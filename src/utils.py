from pprint import pprint

import pandas as pd
from pandas import DataFrame


def xlsx_reader(file_name: str) -> DataFrame:
    """функция чтения данных из таблицы xlsx"""

    result = pd.read_excel("../data/" + file_name)

    return result


if __name__ == "__main__":
    # print(xlsx_reader("operations.xlsx").head())
    pprint(xlsx_reader("operations.xlsx").to_dict("records"))
