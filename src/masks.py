from datetime import datetime


def filter_by_status(transactions, status):
    """Фильтрует список транзакций по статусу"""
    return [t for t in transactions if t.get("status") == status]


def filter_by_word(transactions, word):
    """Фильтрует транзакции по слову в описании"""
    return [t for t in transactions if word.lower() in t.get("description", "").lower()]


def sort_by_date(transactions: list[dict], descending: bool = True) -> list[dict]:
    """Сортирует транзакции по дате."""
    try:
        return sorted(
            transactions,
            key=lambda x: datetime.fromisoformat(x["date"]),
            reverse=descending
        )
    except Exception as e:
        raise ValueError("Неверный формат даты в данных") from e


# Alias для совместимости с тестами
filter_by_state = filter_by_status


# --------------------------
# Функции маскирования
# --------------------------

def get_mask_account(account: str) -> str:
    """Маскирует счет: оставляет только последние 4 цифры"""
    if len(account) != 20 or not account.isdigit():
        raise ValueError("Некорректный номер счета")
    return f"**{account[-4:]}"


def get_mask_card_number(card: str) -> str:
    """Маскирует карту: XXXX XX** **** XXXX"""
    if len(card) != 16 or not card.isdigit():
        raise ValueError("Некорректный номер карты")
    return f"{card[:4]} {card[4:6]}** **** {card[-4:]}"