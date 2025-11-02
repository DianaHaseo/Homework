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


@pytest.mark.parametrize("data,categories,exception", [
    ("not list", ["перевод"], TypeError),
    ([], "перевод", TypeError),
    (123, [], TypeError),
])
def test_statistics_invalid_types(data, categories, exception):
    with pytest.raises(exception):
        process_bank_operations(data, categories)
