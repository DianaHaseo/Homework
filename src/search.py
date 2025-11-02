import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Возвращает список транзакций, в описании которых встречается строка поиска.
    Поиск нечувствителен к регистру.
    """
    if not isinstance(search, str) or not search.strip():
        raise ValueError("Строка поиска должна быть непустой строкой")

    pattern = re.compile(re.escape(search.strip()), re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]
