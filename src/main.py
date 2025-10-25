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
        data = read_json("data/operations.json")
        print("Для обработки выбран JSON-файл.")
    elif file_choice == "2":
        data = read_csv("data/operations.csv")
        print("Для обработки выбран CSV-файл.")
    elif file_choice == "3":
        data = read_xlsx("data/operations.xlsx")
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор файла.")
        return

    if not data:
        print("Не удалось загрузить данные из файла.")
        return

    # Ввод статуса
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

    # Сортировка
    print("\nОтсортировать операции по дате? Да/Нет")
    if input().strip().lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        order = input().strip().lower()
        descending = "убыв" in order
        filtered = sort_by_date(filtered, descending)

    # Фильтр по валюте (рублевые)
    print("\nВыводить только рублевые транзакции? Да/Нет")
    if input().strip().lower() == "да":
        filtered = [t for t in filtered if
                    t.get("operationAmount", {}).get("currency", {}).get("code", "").lower() == "rub"]

    # Фильтр по слову
    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
    if input().strip().lower() == "да":
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
        desc = t.get("description", "")
        amount = t.get("operationAmount", {}).get("amount", "")
        currency = t.get("operationAmount", {}).get("currency", {}).get("code", "")
        from_acc = t.get("from")
        to_acc = t.get("to")

        from_masked = mask_card_or_account(from_acc) if from_acc else ""
        to_masked = mask_card_or_account(to_acc) if to_acc else ""

        print(f"{date_str} {desc}")
        if from_masked and to_masked:
            print(f"{from_masked} -> {to_masked}")
        elif to_masked:
            print(to_masked)
        print(f"Сумма: {amount} {currency}\n")

if __name__ == "__main__":
    main()