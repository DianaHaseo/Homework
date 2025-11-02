from src.masks import get_mask_account, get_mask_card_number
import re
from datetime import datetime


def get_date(date_str: str) -> str:
    """Преобразует дату из формата ISO 'YYYY-MM-DD' или 'YYYY-MM-DDTHH:MM:SS' в 'DD.MM.YYYY'"""
    try:
        date_part = date_str.split("T")[0]
        dt = datetime.strptime(date_part, "%Y-%m-%d")  # строго проверяем формат
        return dt.strftime("%d.%m.%Y")
    except Exception:
        raise ValueError("Некорректный формат даты")


def mask_card_or_account(text: str) -> str:
    """Маскирует карту или счет, определяя тип по ключевым словам"""
    number_match = re.search(r"\d{10,}", text)
    if not number_match:
        raise ValueError("Номер не найден")
    number = number_match.group(0)

    # Если это счет — используем get_mask_account
    if "Счет" in text or len(number) > 16:
        return get_mask_account(number)
    # Если это карта — используем get_mask_card_number
    return get_mask_card_number(number)
