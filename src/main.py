from src.masks import filter_by_status
from src.utils import read_transactions


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        file_name = "data/operations.json"
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        file_name = "data/operations.csv"
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        file_name = "data/operations.xlsx"
    else:
        print("Некорректный выбор файла.")
        return

    data = read_transactions(file_name)
    if not data:
        print("Не удалось загрузить данные из файла.")
        return

    while True:
        status = input("Введите статус для фильтрации (например, EXECUTED, CANCELED): ").strip().upper()
        if status not in ["EXECUTED", "CANCELED"]:
            print(f'Статус операции "{status}" недоступен.')
            continue
        filtered = filter_by_status(data, status)
        print(f'Операции отфильтрованы по статусу "{status}"')
        break

    print("Программа завершена.")


if __name__ == "__main__":
    main()
