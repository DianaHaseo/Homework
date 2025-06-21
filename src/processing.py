def filter_by_state(items: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param items: список словарей, каждый из которых должен содержать ключ 'state'
    :param state: значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED')
    :return: новый список словарей, у которых state == state
    """
    return [item for item in items if item.get('state') == state]


