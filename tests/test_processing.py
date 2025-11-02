import pytest
from src.processing import filter_by_state, sort_by_date


# -----------------------------
# Фикстуры для тестов filter_by_state
# -----------------------------
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


# -----------------------------
# Тест фильтрации по умолчанию
# -----------------------------
def test_filter_by_state_default(sample_transactions):
    filtered = filter_by_state(sample_transactions)  # по умолчанию "EXECUTED"
    assert [item["id"] for item in filtered] == [1, 3, 6]


# -----------------------------
# Параметризованный тест для filter_by_state
# -----------------------------
@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3, 6]),
        ("PENDING", [2]),
        ("CANCELLED", [4]),
        ("MISSING", []),
    ],
)
def test_filter_by_state_parametrized(sample_transactions, state, expected_ids):
    filtered = filter_by_state(sample_transactions, state)
    assert [item["id"] for item in filtered] == expected_ids


# -----------------------------
# Фикстуры для тестов sort_by_date
# -----------------------------
@pytest.fixture
def dated_transactions():
    return [
        {"id": 1, "date": "2023-06-29"},
        {"id": 2, "date": "2022-01-01"},
        {"id": 3, "date": "2023-06-28"},
        {"id": 4, "date": "2023-06-29"},  # повторяющаяся дата
    ]


# -----------------------------
# Параметризованный тест sort_by_date
# -----------------------------
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
