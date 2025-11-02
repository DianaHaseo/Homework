import json
from pathlib import Path


def load_transactions_from_json(path: str | Path) -> list[dict]:
    """Загружает транзакции из JSON файла"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            return []
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
