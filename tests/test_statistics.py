from src.statistics import count_operations_by_categories

transactions = [
    {"description": "Покупка продуктов"},
    {"description": "Перевод на карту"},
    {"description": "Снятие наличных"},
    {"description": "Покупка билетов"},
    {"description": "Пополнение счета"},
]


def test_count_single_category():
    """Проверка подсчета одной категории"""
    categories = ["Покупка"]
    result = count_operations_by_categories(transactions, categories)
    assert result == {"Покупка": 2}


def test_count_multiple_categories():
    """Проверка подсчета нескольких категорий"""
    categories = ["Покупка", "Перевод", "Снятие"]
    result = count_operations_by_categories(transactions, categories)
    assert result == {"Покупка": 2, "Перевод": 1, "Снятие": 1}


def test_count_no_matches():
    """Если категории не встречаются, результат пуст"""
    categories = ["Комиссия", "Штраф"]
    result = count_operations_by_categories(transactions, categories)
    assert result == {}
