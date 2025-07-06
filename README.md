# Домашнее задание 10.1

## Описание:

Домашнее задание - создание программы для работы с банковскими картами

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/DianaHaseo/Homework.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Тестирование

Тестирование нам нужно для проверки правильности выполнения кода.

Для проверки кода можно использовать следующие команды:

Вариант 1. Обычное тестирование для проверки работоспособности теста.
```
pytest
```
Вариант 2. Тестирование для того, чтобы сгенерировать отчет о покрытии в HTML-формате
```
pytest --cov=src --cov-report=html
```

## В проект был добавлен довый модуль generators и тест к нему для проверки работы кода

Для проверки функций filter_by_currency, transaction_descriptions и card_number_generators можно использовать вот такие функции

```
Пример использования для filter_by_currency:

transactions = [
    {"id": 1, "amount": 100, "currency": "USD"},
    {"id": 2, "amount": 200, "currency": "EUR"},
    {"id": 3, "amount": 150, "currency": "USD"},
]

usd_transactions = filter_by_currency(transactions, "USD")
for tx in usd_transactions:
    print(tx)
```

```
Пример использования для transaction_descriptions:

transactions = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Перевод со счета на счет"},
    {"id": 3, "description": "Перевод со счета на счет"},
    {"id": 4, "description": "Перевод с карты на карту"},
    {"id": 5, "description": "Перевод организации"},
]

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
```

```
Пример использования для card_number_generators:

for card_number in card_number_generator(1, 5):
    print(card_number)
```

## Документация:

Для получения дополнительной информации обратитесь к [документации](Homework/README.md).
