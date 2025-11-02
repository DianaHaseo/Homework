import pytest

from src.generators import card_number_generator  # замените your_module на имя вашего модуля
from src.generators import filter_by_currency, transaction_descriptions


# ======== Тесты для filter_by_currency ========

@pytest.fixture
def transactions():
    return [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"},
        {"id": 3, "amount": 150, "currency": "USD"},
        {"id": 4, "amount": 300, "currency": "JPY"},
        {"id": 5, "amount": 50},  # без ключа 'currency'
    ]


@pytest.mark.parametrize("currency, expected_ids", [
    ("USD", [1, 3]),
    ("EUR", [2]),
    ("JPY", [4]),
    ("GBP", []),  # отсутствующая валюта
])
def test_filter_by_currency(transactions, currency, expected_ids):
    filtered = list(filter_by_currency(transactions, currency))
    assert [tx["id"] for tx in filtered] == expected_ids


def test_filter_by_currency_empty_list():
    filtered = list(filter_by_currency([], "USD"))
    assert filtered == []


def test_filter_by_currency_no_matching_currency():
    transactions = [{"id": 1, "currency": "EUR"}]
    filtered = list(filter_by_currency(transactions, "USD"))
    assert filtered == []


# ======== Тесты для transaction_descriptions ========

@pytest.fixture
def transactions_with_descriptions():
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Оплата услуг"},
    ]


def test_transaction_descriptions_correct_output(transactions_with_descriptions):
    gen = transaction_descriptions(transactions_with_descriptions)
    descriptions = list(gen)
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Оплата услуг",
    ]
    assert descriptions == expected


def test_transaction_descriptions_empty_list():
    gen = transaction_descriptions([])
    assert list(gen) == []


def test_transaction_descriptions_missing_description():
    transactions = [
        {"id": 1},
        {"id": 2, "description": "Оплата"},
    ]
    gen = transaction_descriptions(transactions)
    descriptions = list(gen)
    assert descriptions == ["", "Оплата"]


# ======== Тесты для card_number_generator ========

@pytest.mark.parametrize("start, end, expected", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]),
    (9999999999999995, 9999999999999999, [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]),
])
def test_card_number_generator_range(start, end, expected):
    gen = card_number_generator(start, end)
    result = list(gen)
    assert result == expected


def test_card_number_generator_formatting():
    gen = card_number_generator(1, 1)
    card_number = next(gen)
    assert len(card_number) == 19  # 16 цифр + 3 пробела
    assert card_number.count(' ') == 3
    parts = card_number.split(' ')
    assert all(len(part) == 4 for part in parts)
    assert card_number == "0000 0000 0000 0001"


def test_card_number_generator_empty_range():
    gen = card_number_generator(5, 4)
    assert list(gen) == []  # пустой генератор, если start > end
