import json


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
