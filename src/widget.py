from src.masks import get_mask_account, get_mask_card_number
import re
from datetime import datetime

def mask_card_or_account(full_string: str) -> str:
    # Ищем номер — последовательность из 10 и более цифр
    match = re.search(r'\d{10,}', full_string)
    if not match:
        raise ValueError("Номер карты или счета не найден в строке")
    number = match.group(0)
    # Определяем тип по наличию слова "Счет"
    if 'Счет' in full_string:
        return get_mask_account(number)
    else:
        return get_mask_card_number(number)

def get_date(date_str: str) -> str:
    dt = datetime.fromisoformat(date_str)
    return dt.strftime('%d.%m.%Y')
