import builtins
import pytest
from src.main import main


@pytest.fixture
def mock_data(monkeypatch):
    """Мокаем ввод пользователя и перехватываем вывод."""
    inputs = iter([
        "1",  # выбор JSON
        "EXECUTED",  # фильтр по статусу
        "да",  # сортировка по дате
        "по возрастанию",
        "нет",  # не фильтровать по слову
    ])
    monkeypatch.setattr(builtins, "input", lambda *args: next(inputs))

    printed = []
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: printed.append(" ".join(map(str, args))))
    return printed


def test_main_successful_run(mock_data):
    """Проверяет корректный сценарий main()."""
    main()
    assert any("Привет!" in line for line in mock_data)
    assert any("Операции отфильтрованы по статусу" in line for line in mock_data)
    assert any("Программа завершена." in line for line in mock_data)


def test_main_invalid_status(monkeypatch):
    """Проверяет обработку некорректного статуса пользователя."""
    inputs = iter([
        "1",  # выбор файла JSON
        "TEST",  # неверный статус
        "EXECUTED",  # потом правильный
        "нет",  # не сортировать
        "нет",  # не фильтровать
    ])
    printed = []
    monkeypatch.setattr(builtins, "input", lambda *args: next(inputs))
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: printed.append(" ".join(map(str, args))))

    main()

    assert any('Статус операции "TEST" недоступен.' in line for line in printed)
    assert any("Операции отфильтрованы по статусу" in line for line in printed)
