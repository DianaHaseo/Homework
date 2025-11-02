import pytest
from src.search import process_bank_search


@pytest.fixture
def transactions_data():
    return [
        {"description": "Перевод организации", "amount": 5000},
        {"description": "Открытие вклада", "amount": 10000},
        {"description": "Перевод на карту", "amount": 2500},
        {"description": "Пополнение счета", "amount": 3000},
    ]


def test_search_single_match(transactions_data):
    result = process_bank_search(transactions_data, "вклад")
    assert len(result) == 1
    assert result[0]["description"] == "Открытие вклада"


def test_search_multiple_matches(transactions_data):
    result = process_bank_search(transactions_data, "перевод")
    assert len(result) == 2
    assert all("перевод" in item["description"].lower() for item in result)


def test_search_case_insensitive(transactions_data):
    result = process_bank_search(transactions_data, "ПЕРЕВОД")
    assert len(result) == 2


def test_search_no_match(transactions_data):
    result = process_bank_search(transactions_data, "неизвестно")
    assert result == []


@pytest.mark.parametrize("invalid_input", [None, "", 123, [], {}])
def test_search_invalid_input(transactions_data, invalid_input):
    with pytest.raises(ValueError):
        process_bank_search(transactions_data, invalid_input)
