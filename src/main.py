from src.utils import read_json, read_csv, read_xlsx
from src.processing import filter_by_status, sort_by_date
from src.widget import get_date
from src.masks import mask_card_or_account


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input().strip()

    if file_choice == "1":
        data = read_json("data.json")
        print("Для обработки выбран JSON-файл.")
    elif file_choice == "2":
        data = read_csv("data.csv")
        print("Для обработки выбран CSV-файл.")
    elif file_choice == "3":
        data = read_xlsx("data.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор файла")
        return

    # Проверка статуса
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы:", ", ".join(valid_statuses))
        status = input().strip().upper()
        if status in valid_statuses:
            filtered = filter_by_status(data, status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    # Сортировка по дате
    print("\nОтсортировать операции по дате? Да/Нет")
    sort_choice = input().strip().lower()
    if sort_choice == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        order = input().strip().lower()
        descending = True
        if "возрастанию" in order:
            descending = False
        filtered = sort_by_date(filtered, descending)

    # Фильтр по рублевым
    print("\nВыводить только рублевые транзакции? Да/Нет")
    rub_choice = input().strip().lower()
    if rub_choice == "да":
        filtered = [t for t in filtered if str(t.get("amount", "")).endswith("руб.")]

    # Фильтр по слову
    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
    word_choice = input().strip().lower()
    if word_choice == "да":
        print("Введите слово для фильтрации:")
        word = input().strip().lower()
        filtered = [t for t in filtered if word in t.get("description", "").lower()]

    print("\nРаспечатываю итоговый список транзакций...")
    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(filtered)}\n")

    for t in filtered:
        date_str = get_date(t.get("date", ""))
        description = t.get("description", "")
        amount = t.get("amount", "")
        currency = t.get("currency", "руб.")  # если нет валюты

        # Маскировка счетов и карт
        try:
            description = mask_card_or_account(description)
        except ValueError:
            pass

        print(f"{date_str} {t.get('description')}")
        print(f"{description}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()