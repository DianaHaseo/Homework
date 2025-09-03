import json
from typing import List, Dict, Any

def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.

    :param file_path: путь до JSON-файла
    :return: список словарей или пустой список при ошибках/несоответствии
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, list):
            return []
        if not all(isinstance(item, dict) for item in data):
            return []
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []