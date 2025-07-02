import datetime
import json
import logging
from functools import wraps
from typing import Any, Callable, Optional

from dateutil.relativedelta import relativedelta
from pandas import DataFrame

from config import BASE_PATH
from src.utils import xlsx_reader

CUR_DATE = datetime.datetime.now().strftime("%d.%m.%Y")

# имя файла отчета по умолчанию с привязкой к текущей дате
default_name = f"report_{CUR_DATE}.json"

# инициализация логгера в модуле
func_logger = logging.getLogger("func_logger")
func_logger.setLevel(logging.DEBUG)
file_func_handler = logging.FileHandler(f"{BASE_PATH}/logs/func_log.log", mode="a")
file_func_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_func_handler.setFormatter(file_func_formatter)
func_logger.addHandler(file_func_handler)


def report_to_file(file_name: Optional = default_name) -> Callable:
    """декоратор для записи отчета в файл"""

    def decor(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = function(*args, **kwargs)

            with open(f"{BASE_PATH}/reports/{file_name}", "w") as f:
                json.dump(result, f, ensure_ascii=False)

            return result

        return wrapper

    return decor


@report_to_file()
def category_cost(transactions: DataFrame, category: str, date: str = CUR_DATE) -> str:
    """функция подсчитывает траты по операциям в заданной категории за 3 месяца с указанной даты"""

    func_logger.info("обращение к функции - category_cost")

    # преобразование DataFrame в список словарей для удобства работы
    list_transactions = transactions.to_dict("records")

    # создание списка транзакций подходящих условию по даты
    date_gr_1 = datetime.datetime.strptime(date, "%d.%m.%Y")  # верхняя граница даты
    date_gr_2 = date_gr_1 - relativedelta(months=3)  # нижняя граница даты

    func_logger.info("обработка данных функцией - category_cost")

    lst_trans_date = []

    for trans in list_transactions:
        lst_trans = trans["Дата операции"].split(" ")
        date_trans = datetime.datetime.strptime(lst_trans[0], "%d.%m.%Y")
        if date_gr_2 < date_trans < date_gr_1:
            lst_trans_date.append(trans)

    # создание списка транзакций подходящих под нужную категорию
    result = sum([trans["Сумма операции"] for trans in lst_trans_date if trans["Категория"] == category])

    func_logger.info("вывод результатов функцией category_cost")

    # проверка вывода суммы затрат на отсутствие затрат и приход/уход средств и вывод результата
    if result == 0:
        return f"По категории - {category} в указанный период трат не было"
    elif result > 0:
        return f"По категории - {category} в указанном периоде получено: {result} руб"
    else:
        return f"По категории - {category} в указанном периоде потрачено: {abs(result)} руб"


if __name__ == "__main__":
    lst = category_cost(xlsx_reader("operations.xlsx"), "Красота", "11.06.2018")
    print(lst)
