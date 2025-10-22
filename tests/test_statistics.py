import pytest
from src.statistics import process_bank_operations


@pytest.fixture
def sample_data():
    return [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод на карту"},
        {"description": "Пополнение счета"},
    ]


def test_statistics_basic(sample_data):
    categories = ["перевод", "вклад"]
    result = process_bank_operations(sample_data, categories)
    assert result == {"перевод": 2, "вклад": 1}


def test_statistics_case_insensitive(sample_data):
    categories = ["ПЕРЕВОД", "вКЛАД"]
    result = process_bank_operations(sample_data, categories)
    assert result == {"ПЕРЕВОД": 2, "вКЛАД": 1}


def test_statistics_no_matches(sample_data):
    categories = ["покупка", "оплата"]
    result = process_bank_operations(sample_data, categories)
    assert result == {"покупка": 0, "оплата": 0}


def test_statistics_invalid_data_type():
    with pytest.raises(TypeError):
        process_bank_operations("не список", ["перевод"])


def test_statistics_invalid_categories_type(sample_data):
    with pytest.raises(TypeError):
        process_bank_operations(sample_data, "вклад")