import re
import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_card_or_account


# -------------------------------
# Фикстура для тестирования mask_card_or_account
# -------------------------------
@pytest.fixture(
    params=[
        # счета (20 цифр или слово "Счет")
        ("Перевод на Счет 40817810099910004312", get_mask_account),
        ("Оплата по Счету 12345678901234567890", get_mask_account),
        ("Номер счета: 00000000000000000001", get_mask_account),

        # карты (16 цифр или слово "карта")
        ("Оплата картой 4276380000000000", get_mask_card_number),
        ("Перевод с карты 1234567890123456", get_mask_card_number),

        # длинный номер (>16 цифр) с "карта" → считается счетом
        ("Номер карты: 12345678901234567890", get_mask_account),
    ]
)
def card_or_account_data(request):
    return request.param


# фикстура для невалидных данных
@pytest.fixture(
    params=[
        "В этой строке нет номера",
        "Номер 123456789",  # меньше 10 цифр
        "Счет 123",  # слишком короткий номер
    ]
)
def invalid_card_or_account_data(request):
    return request.param


# -------------------------------
# Тесты для mask_card_or_account
# -------------------------------
def test_mask_card_or_account(card_or_account_data):
    input_str, expected_mask_func = card_or_account_data
    masked = mask_card_or_account(input_str)
    number = re.search(r"\d{10,}", input_str).group(0)
    expected = expected_mask_func(number)
    assert masked == expected


def test_mask_card_or_account_invalid(invalid_card_or_account_data):
    with pytest.raises(ValueError):
        mask_card_or_account(invalid_card_or_account_data)


# -------------------------------
# Фикстуры для тестирования get_date
# -------------------------------
@pytest.fixture(
    params=[
        ("2023-06-29", "29.06.2023"),
        ("2023-01-01", "01.01.2023"),
        ("2020-02-29", "29.02.2020"),
        ("2023-12-31", "31.12.2023"),
        ("2023-06-29T15:45:00", "29.06.2023"),
    ]
)
def valid_date_data(request):
    return request.param


@pytest.fixture(
    params=[
        "",
        "not a date",
        "2023/06/29",
        "29-06-2023",
        None,
    ]
)
def invalid_date_data(request):
    return request.param


# -------------------------------
# Тесты для get_date
# -------------------------------
def test_get_date_valid(valid_date_data):
    input_str, expected = valid_date_data
    assert get_date(input_str) == expected


def test_get_date_invalid(invalid_date_data):
    with pytest.raises(ValueError):
        get_date(invalid_date_data)
