def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    """
    Возвращает словарь с количеством операций по категориям (по description).
    """
    if not isinstance(data, list):
        raise TypeError("Данные должны быть списком словарей")

    if not isinstance(categories, list):
        raise TypeError("Список категорий должен быть списком строк")

    result = {category: 0 for category in categories}

    for item in data:
        desc = item.get("description", "").lower()
        for category in categories:
            if category.lower() in desc:
                result[category] += 1

    return result
