import pytest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub

@patch("src.external_api.requests.get")
def test_convert_to_rub_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 60.0}}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    result = convert_to_rub(10, "USD")
    assert result == 600.0
    mock_get.assert_called_once()

@patch("src.external_api.requests.get")
def test_convert_to_rub_no_rate(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {}}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    with pytest.raises(Exception, match="Курс RUB для валюты USD не найден"):
        convert_to_rub(10, "USD")

def test_convert_to_rub_invalid_currency():
    with pytest.raises(ValueError):
        convert_to_rub(10, "GBP")
