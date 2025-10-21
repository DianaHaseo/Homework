import re
from typing import List, Dict, Any


def search_transactions_by_description(transactions: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    """
    Ищет операции, в описании которых содержится заданная строка (поиск без учёта регистра, с помощью re).

    :param transactions: список транзакций (каждая транзакция — словарь с ключом 'description')
    :param query: строка для поиска
    :return: список транзакций, в описании которых найдено совпадение
    """
    pattern = re.compile(query, re.IGNORECASE)
    result = [tx for tx in transactions if 'description' in tx and pattern.search(str(tx['description']))]
    return result
