from collections import Counter
from typing import List, Dict, Any


def count_operations_by_categories(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям на основе поля 'description'.

    :param transactions: список транзакций (каждая транзакция — словарь с ключом 'description')
    :param categories: список категорий (слов, по которым искать совпадения в описании)
    :return: словарь вида {категория: количество операций}
    """
    counter = Counter()

    for tx in transactions:
        description = str(tx.get('description', '')).lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1

    return dict(counter)