import pandas as pd
import pandas.testing as tm

from src.utils import xlsx_reader


def test_xlsx_reader(mocker):
    """тестирование функции считывающей данные из xlsx таблиц"""

    # тест на нормальное открытие файла
    test_data = [{"id": 650703.0, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    test_dataframe = pd.DataFrame(test_data)
    mocker.patch("pandas.read_excel", return_value=pd.DataFrame(test_data))
    result = xlsx_reader("operations.xlsx")

    tm.assert_frame_equal(result, test_dataframe)
