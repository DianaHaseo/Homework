from src.external_api import convert_to_rub

def get_transaction_amount_in_rub(transaction: dict) -> float:
    """
    Возвращает сумму транзакции в рублях; при валюте USD/EUR конвертирует через API.

    :param transaction: словарь с ключами 'amount' и 'currency'
    :return: сумма в рублях (float)
    """
    amount = float(transaction.get('amount', 0))
    currency = transaction.get('currency', 'RUB').upper()

    if currency in ("USD", "EUR"):
        return convert_to_rub(amount, currency)
    else:
        return amount
