from datetime import datetime

def filter_by_status(transactions: list[dict], status: str = "EXECUTED") -> list[dict]:
    """Фильтрует транзакции по статусу."""
    return [t for t in transactions if t.get("state") == status]

# Alias для совместимости с тестами
filter_by_state = filter_by_status


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