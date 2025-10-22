import re
from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number

def mask_card_or_account(text: str) -> str:
    if not text:
        return ""
    digits = re.findall(r"\d+", text)
    if not digits:
        return text
    number = digits[0]
    if len(number) >= 16:
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    else:
        return f"**{number[-4:]}"


from src.masks import mask_card_or_account
from datetime import datetime

def get_date(date_str: str) -> str:
    """Преобразует дату в формат DD.MM.YYYY"""
    if not date_str:
        raise ValueError("Пустая строка даты")
    if "T" in date_str:  # ISO с временем
        date_str = date_str.split("T")[0]
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except Exception:
        raise ValueError("Неверный формат даты")