import builtins
import pytest
from src.search import search_transactions_by_description
from src.statistics import count_operations_by_categories

# Пример данных, которые могли бы быть загружены из файла
transactions = [
    {"date": "2023-01-01", "description": "Покупка продуктов", "amount": "1500", "currency": "RUB"},
    {"date": "2023-02-10", "description": "Перевод другу", "amount": "200", "currency": "USD"},
    {"date": "2023-03-05", "description": "Снятие наличных в банкомате", "amount": "5000", "currency": "RUB"},
]


def test_search_integration():
    """Интеграционный тест: проверяем связку поиска и данных"""
    result = search_transactions_by_description(transactions, "продукт")
    assert len(result) == 1
    assert result[0]["description"] == "Покупка продуктов"


def test_statistics_integration():
    """Интеграционный тест: проверяем подсчет категорий"""
    categories = ["Покупка", "Снятие"]
    result = count_operations_by_categories(transactions, categories)
    assert result == {"Покупка": 1, "Снятие": 1}