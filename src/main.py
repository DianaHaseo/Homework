import sys
from src.utils import load_transactions_from_json
from src.transactions_io import read_transactions_from_csv, read_transactions_from_excel
from src.search import search_transactions_by_description
from src.statistics import count_operations_by_categories


def main():
    """
    Главная функция, связывающая все функции проекта.
    Позволяет пользователю:
      1. Загрузить транзакции из файла (JSON, CSV или Excel)
      2. Выполнить поиск по описанию
      3. Подсчитать количество операций по категориям
    """
    print("Добро пожаловать в систему анализа транзакций!\n")

    # --- Загрузка данных ---
    file_path = input("Введите путь к файлу с транзакциями (.json / .csv / .xlsx): ").strip()

    if file_path.endswith(".json"):
        transactions = load_transactions_from_json(file_path)
    elif file_path.endswith(".csv"):
        transactions = read_transactions_from_csv(file_path)
    elif file_path.endswith(".xlsx"):
        transactions = read_transactions_from_excel(file_path)
    else:
        print("Неподдерживаемый формат файла. Допустимые форматы: JSON, CSV, XLSX.")
        sys.exit(1)

    if not transactions:
        print("Ошибка: не удалось загрузить транзакции или файл пуст.")
        sys.exit(1)

    print(f"Загружено {len(transactions)} транзакций.\n")

    # --- Меню действий ---
    while True:
        print("Выберите действие:")
        print("1. Поиск операций по описанию")
        print("2. Подсчет количества операций по категориям")
        print("3. Выход")
        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            query = input("Введите строку для поиска в описаниях: ").strip()
            found = search_transactions_by_description(transactions, query)
            print(f"Найдено {len(found)} операций:")
            for tx in found:
                print(f"- {tx.get('date', '')}: {tx.get('description', '')} ({tx.get('amount', '')} {tx.get('currency', '')})")
            print()

        elif choice == "2":
            cats_input = input("Введите категории через запятую (например: Перевод, Покупка, Снятие): ").strip()
            categories = [cat.strip() for cat in cats_input.split(",") if cat.strip()]
            result = count_operations_by_categories(transactions, categories)
            print("\nКоличество операций по категориям:")
            for cat, count in result.items():
                print(f"- {cat}: {count}")
            print()

        elif choice == "3":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный выбор. Повторите попытку.\n")

if __name__ == "__main__":
    main()
