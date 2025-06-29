import pytest
from src.masks import get_mask_account, get_mask_card_number

# Тесты для get_mask_card_number
@pytest.mark.parametrize("input_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),           # стандартный 16-значный номер
    ("1234 56 7890 1234", "1234 56** **** 1234"),          # с пробелами
    ("1234567890", "1234 56** **** 7890"),                  # минимальная длина 10
    ("12345678901234567890", "1234 56** **** 7890"),        # длиннее 16, маска по первым 6 и последним 4
])
def test_get_mask_card_number_valid(input_number, expected):
    assert get_mask_card_number(input_number) == expected

@pytest.mark.parametrize("invalid_input", [
    "",             # пустая строка
    "123456789",    # меньше 10 цифр
    "abcd1234efg",  # буквы и цифры, но меньше 10 цифр
])
def test_get_mask_card_number_invalid(invalid_input):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_input)

# Тесты для get_mask_account
@pytest.mark.parametrize("input_number, expected", [
    ("1234567890", "**7890"),          # стандартный номер
    ("  9876543210  ", "**3210"),      # с пробелами
    ("1234", "**1234"),                # ровно 4 цифры
    ("123456", "**3456"),              # больше 4 цифр
])
def test_get_mask_account_valid(input_number, expected):
    assert get_mask_account(input_number) == expected

@pytest.mark.parametrize("invalid_input", [
    "",         # пустая строка
    "123",      # меньше 4 цифр
    "abc",      # буквы
    "12 3",     # меньше 4 цифр с пробелами
])
def test_get_mask_account_invalid(invalid_input):
    with pytest.raises(ValueError):
        get_mask_account(invalid_input)