import pytest
from src.search import search_transactions_by_description

# Пример списка транзакций для тестов
transactions = [
    {"date": "2023-01-10", "description": "Оплата покупок в магазине", "amount": "1000", "currency": "RUB"},
    {"date": "2023-02-01", "description": "Перевод другу", "amount": "200", "currency": "USD"},
    {"date": "2023-03-15", "description": "Покупка билетов на поезд", "amount": "3000", "currency": "RUB"},
]


def test_search_exact_word():
    """Проверяет, что поиск находит точное слово в описании"""
    result = search_transactions_by_description(transactions, "магазине")
    assert len(result) == 1
    assert result[0]["description"] == "Оплата покупок в магазине"


def test_search_case_insensitive():
    """Поиск должен быть нечувствительным к регистру"""
    result = search_transactions_by_description(transactions, "ПОКУПКА")
    assert len(result) == 1
    assert "Покупка" in result[0]["description"]


def test_search_multiple_matches():
    """Если совпадений несколько — все они возвращаются"""
    result = search_transactions_by_description(transactions, "покуп")
    assert len(result) == 2  # 'покупок' и 'Покупка билетов...'


def test_search_no_matches():
    """Если совпадений нет — возвращается пустой список"""
    result = search_transactions_by_description(transactions, "не существует")
    assert result == []