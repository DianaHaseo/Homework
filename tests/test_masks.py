import pytest
from src.masks import get_mask_account, get_mask_card_number


# Фикстура для тестовых данных карт (ровно 16 цифр)
@pytest.fixture(
    params=[
        ("1234567890123456", "1234 56** **** 3456"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("4000123412341234", "4000 12** **** 1234"),
    ]
)
def valid_card_data(request):
    return request.param

@pytest.fixture(
    params=[
        # Счета (20 цифр или слово "Счет")
        ("Перевод на Счет 40817810099910004312", get_mask_account),
        ("Оплата по Счету 12345678901234567890", get_mask_account),
        ("Номер счета: 00000000000000000001", get_mask_account),

        # Карты (16 цифр или слово "карта")
        ("Оплата картой 4276380000000000", get_mask_card_number),
        ("Перевод с карты 1234567890123456", get_mask_card_number),

        # Длинный номер с "карта" (>16 цифр) — это всё равно счет
        ("Номер карты: 12345678901234567890", get_mask_account),  # <-- исправлено
    ]
)
def card_or_account_data(request):
    return request.param

@pytest.fixture(params=[
    "",        # пусто
    "123",     # слишком короткий
    "abc123",  # буквы
])
def invalid_card_data(request):
    return request.param


# Фикстура для тестовых данных счетов (ровно 20 цифр)
@pytest.fixture(
    params=[
        ("12345678901234567890", "**7890"),
        ("40817810099910004312", "**4312"),
        ("00000000000000000001", "**0001"),
    ]
)
def valid_account_data(request):
    return request.param


@pytest.fixture(
    params=[
        "",                 # пусто
        "123",              # слишком короткий
        "123456789",        # недостаточно цифр
        "123456789012345",  # 15 цифр
        "abcd1234",         # буквы
    ]
)
def invalid_account_data(request):
    return request.param


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

