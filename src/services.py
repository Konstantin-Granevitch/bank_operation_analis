import json
import re


def finder(list_transactions: list[dict], attribute: str) -> str:
    """функция поиска транзакций по условию в виде строки"""

    result = []

    for transaction in list_transactions:
        if attribute in str(transaction):
            result.append(transaction)

    if result == []:
        return "искомые транзакции отсутствуют"
    else:
        return json.dumps(result, ensure_ascii=False)


def tel_finder(list_transactions: list[dict]) -> str:
    """Функция поиска транзакций в описании которых присутствуют телефонные номера"""

    tel_number = re.compile(r"[+]\d\s\d{3}.\d{2}.\d{2}")
    result = []

    for transaction in list_transactions:
        if re.search(tel_number, str(transaction)):
            result.append(transaction)

    if result == []:
        return "транзакции с телефонными номерами отсутствуют"
    else:
        return json.dumps(result, ensure_ascii=False)
