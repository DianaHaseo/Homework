import re
from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_card_or_account(full_string: str) -> str:
    """
    Определяет, какой тип данных в строке — карта или счёт — и возвращает замаскированный номер.
    """
    if not isinstance(full_string, str):
        raise ValueError("Входные данные должны быть строкой")

    match = re.search(r"\d{10,}", full_string)
    if not match:
        raise ValueError("Номер карты или счета не найден")

    number = match.group(0)
    text = full_string.lower()

    if "счет" in text:
        return get_mask_account(number)
    elif "карта" in text:
        return get_mask_card_number(number)

    if len(number) == 16:
        return get_mask_card_number(number)
    elif len(number) == 20:
        return get_mask_account(number)

    raise ValueError("Не удалось определить тип номера")


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата 'YYYY-MM-DD' или 'YYYY-MM-DDTHH:MM:SS' в 'DD.MM.YYYY'.
    """
    if not date_string or not isinstance(date_string, str):
        raise TypeError("Дата должна быть строкой")

    try:
        date_part = date_string.split("T")[0]
        parsed_date = datetime.strptime(date_part, "%Y-%m-%d")
        return parsed_date.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError(f"Неверный формат даты: {date_string}")