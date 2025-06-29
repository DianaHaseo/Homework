import re
import pytest
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_card_or_account, get_date  # замените your_module на имя вашего модуля

# Тесты для mask_card_or_account
@pytest.mark.parametrize("input_str, expected_mask_func", [
    # Тесты для счетов (есть слово "Счет")
    ("Перевод на Счет 40817810099910004312", get_mask_account),
    ("Оплата по Счету 12345678901234567890", get_mask_account),
    # Тесты для карт (нет слова "Счет")
    ("Оплата картой 4276380000000000", get_mask_card_number),
    ("Перевод с карты 1234567890123456", get_mask_card_number),
    ("Номер карты: 12345678901234567890", get_mask_card_number),
])
def test_mask_card_or_account(input_str, expected_mask_func):
    masked = mask_card_or_account(input_str)
    number = re.search(r'\d{10,}', input_str).group(0)
    expected = expected_mask_func(number)
    assert masked == expected

def test_mask_card_or_account_no_number():
    with pytest.raises(ValueError, match="Номер карты или счета не найден в строке"):
        mask_card_or_account("В этой строке нет номера")

def test_mask_card_or_account_short_number():
    with pytest.raises(ValueError):
        mask_card_or_account("Номер 123456789")  # меньше 10 цифр

# Тесты для get_date
@pytest.mark.parametrize("input_str, expected", [
    ("2023-06-29", "29.06.2023"),           # стандартный ISO формат
    ("2023-01-01", "01.01.2023"),           # начало года
    ("2020-02-29", "29.02.2020"),           # високосный год
    ("2023-12-31", "31.12.2023"),           # конец года
    ("2023-06-29T15:45:00", "29.06.2023"), # ISO с временем
])
def test_get_date_valid(input_str, expected):
    assert get_date(input_str) == expected

@pytest.mark.parametrize("invalid_input", [
    "",                 # пустая строка
    "not a date",       # произвольный текст
    "2023/06/29",       # неправильный формат
    "29-06-2023",       # неправильный формат
    None,               # None вместо строки
])
def test_get_date_invalid(invalid_input):
    with pytest.raises((ValueError, TypeError)):
        get_date(invalid_input)