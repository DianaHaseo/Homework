from datetime import datetime


def filter_by_state(transactions, state="EXECUTED"):
    """Фильтрует список транзакций по состоянию (по умолчанию EXECUTED)"""
    return [t for t in transactions if t.get("state") == state]


# Alias для совместимости со старым кодом / тестами
filter_by_status = filter_by_state


def filter_by_word(transactions, word):
    """Фильтрует транзакции по слову в описании"""
    return [t for t in transactions if word.lower() in t.get("description", "").lower()]


def sort_by_date(transactions: list[dict], descending: bool = True) -> list[dict]:
    """Сортирует транзакции по дате"""
    try:
        return sorted(
            transactions,
            key=lambda x: datetime.fromisoformat(x["date"]),
            reverse=descending
        )
    except Exception as e:
        raise ValueError("Неверный формат даты в данных") from e