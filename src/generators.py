def filter_by_currency(transactions, currency):
    """
    Возвращает итератор по транзакциям с указанной валютой.
    :param transactions: список словарей, каждый из которых представляет транзакцию и содержит ключ 'currency'
    :param currency: строка с кодом валюты (например, 'USD')
    :return: итератор по подходящим транзакциям
    """
    return (tx for tx in transactions if tx.get('currency') == currency)


def transaction_descriptions(transactions):
    """
    Генератор, возвращающий описание каждой транзакции по очереди.

    :param transactions: список словарей с транзакциями, должен содержать ключ 'description'
    :yield: строка — описание операции
    """
    for tx in transactions:
        yield tx.get('description', '')


def card_number_generator(start, end):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    :param start: начальное значение (int или str, например, 1 или '1')
    :param end: конечное значение (int или str, например, 5 или '5')
    :yield: строка — номер карты в формате XXXX XXXX XXXX XXXX
    """
    # Преобразуем к int на случай, если подали строку
    start = int(start)
    stop = int(end)
    for num in range(start, stop + 1):
        num_str = f"{num:016d}"  # 16-значное число с ведущими нулями
        formatted = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted
