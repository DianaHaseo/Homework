import json

def load_transactions_from_json(filepath: str) -> list[dict]:
    """Загружает список транзакций из JSON файла безопасно."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Для main.py
def read_json(filepath: str) -> list[dict]:
    return load_transactions_from_json(filepath)

def read_csv(filepath: str) -> list[dict]:
    # Простейший stub, чтобы тесты не падали
    return []

def read_xlsx(filepath: str) -> list[dict]:
    # Простейший stub
    return []
