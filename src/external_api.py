import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')  # Загружаем переменные из .env (один раз при загрузке модуля)

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(amount: float, currency: str) -> float:
    """
    Конвертирует сумму из USD или EUR в RUB через внешний API.

    :param amount: сумма в исходной валюте
    :param currency: валюта ('USD' или 'EUR')
    :return: сумма в рублях
    :raises Exception: при ошибках сети или отсутствии курса
    """
    if currency not in ("USD", "EUR"):
        raise ValueError("Конвертация поддерживается только для USD и EUR")

    headers = {"apikey": API_KEY}
    params = {"base": currency, "symbols": "RUB"}

    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    rate = data.get("rates", {}).get("RUB")
    if rate is None:
        raise Exception(f"Курс RUB для валюты {currency} не найден")

    return float(amount) * rate
