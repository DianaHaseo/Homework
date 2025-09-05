import pytest
from src.processing import filter_by_state, sort_by_date


# Фикстуры для тестов filter_by_state
@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "CANCELLED"},
        {"id": 5},  # без ключа 'state'
        {"id": 6, "state": "EXECUTED"},
    ]


@pytest.fixture
def empty_transactions():
    return []


# Параметризация для filter_by_state
@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3, 6]),
        ("PENDING", [2]),
        ("CANCELLED", [4]),
        ("MISSING", []),
    ],
)
def test_filter_by_state(sample_transactions, state, expected_ids):
    filtered = filter_by_state(sample_transactions, state)
    assert [item["id"] for item in filtered] == expected_ids


def test_filter_by_state_empty(empty_transactions):
    assert filter_by_state(empty_transactions, "EXECUTED") == []


def test_filter_by_state_default(sample_transactions):
    filtered = filter_by_state(sample_transactions)
    assert [item["id"] for item in filtered] == [1, 3, 6]


# Фикстуры для тестов sort_by_date
@pytest.fixture
def dated_transactions():
    return [
        {"id": 1, "date": "2023-06-29"},
        {"id": 2, "date": "2022-01-01"},
        {"id": 3, "date": "2023-06-28"},
        {"id": 4, "date": "2023-06-29"},  # повторяющаяся дата
    ]


# Параметризация для sort_by_date
@pytest.mark.parametrize(
    "descending, expected_order",
    [
        (True, [1, 4, 3, 2]),  # по убыванию
        (False, [2, 3, 1, 4]),  # по возрастанию
    ],
)
def test_sort_by_date(dated_transactions, descending, expected_order):
    sorted_items = sort_by_date(dated_transactions, descending)
    assert [item["id"] for item in sorted_items] == expected_order


# Тесты для обработки ошибок
@pytest.mark.parametrize(
    "invalid_data",
    [
        [{"id": 1, "date": "29-06-2023"}],
        [{"id": 2, "date": "2023/06/29"}],
        [{"id": 3, "date": "invalid-date"}],
        [{"id": 4, "date": ""}],
    ],
)
def test_sort_by_date_invalid_format(invalid_data):
    with pytest.raises(ValueError):
        sort_by_date(invalid_data)
