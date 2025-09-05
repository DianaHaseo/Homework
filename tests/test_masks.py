import pytest
from src.masks import get_mask_account, get_mask_card_number


# Фикстура для тестовых данных карт
@pytest.fixture(
    params=[
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234 56 7890 1234", "1234 56** **** 1234"),
        ("1234567890", "1234 56** **** 7890"),
        ("12345678901234567890", "1234 56** **** 7890"),
    ]
)
def valid_card_data(request):
    return request.param


# Фикстура для невалидных данных карт
@pytest.fixture(
    params=[
        "",
        "123456789",
        "abcd1234efg",
    ]
)
def invalid_card_data(request):
    return request.param


# Фикстура для тестовых данных счетов
@pytest.fixture(
    params=[
        ("1234567890", "**7890"),
        ("  9876543210  ", "**3210"),
        ("1234", "**1234"),
        ("123456", "**3456"),
    ]
)
def valid_account_data(request):
    return request.param


# Фикстура для невалидных данных счетов
@pytest.fixture(
    params=[
        "",
        "123",
        "abc",
        "12 3",
    ]
)
def invalid_account_data(request):
    return request.param


# Параметризованные тесты с использованием фикстур
def test_get_mask_card_number_valid(valid_card_data):
    input_number, expected = valid_card_data
    assert get_mask_card_number(input_number) == expected


def test_get_mask_card_number_invalid(invalid_card_data):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card_data)


def test_get_mask_account_valid(valid_account_data):
    input_number, expected = valid_account_data
    assert get_mask_account(input_number) == expected


def test_get_mask_account_invalid(invalid_account_data):
    with pytest.raises(ValueError):
        get_mask_account(invalid_account_data)
