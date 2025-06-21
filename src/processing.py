def filter_by_state(items: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param items: список словарей, каждый из которых должен содержать ключ 'state'
    :param state: значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED')
    :return: новый список словарей, у которых state == state
    """
    return [item for item in items if item.get('state') == state]

from datetime import datetime
from typing import List, Dict, Optional

def sort_by_date(items: List[Dict], descending: Optional[bool] = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param items: список словарей, каждый из которых содержит ключ 'date' в формате ISO 8601
    :param descending: порядок сортировки, True - по убыванию (по умолчанию), False - по возрастанию
    :return: новый список словарей, отсортированный по дате
    """
    return sorted(items, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)
