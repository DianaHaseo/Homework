import pytest
from unittest.mock import patch
from src.transactions import get_transaction_amount_in_rub

@patch("src.transactions.convert_to_rub")
def test_get_transaction_amount_in_rub_usd(mock_convert):
    mock_convert.return_value = 700.0
    tx = {"amount": 10, "currency": "USD"}

    result = get_transaction_amount_in_rub(tx)
    assert result == 700.0
    mock_convert.assert_called_once_with(10.0, "USD")

def test_get_transaction_amount_in_rub_rub():
    tx = {"amount": 500, "currency": "RUB"}

    result = get_transaction_amount_in_rub(tx)
    assert result == 500.0

def test_get_transaction_amount_in_rub_default_currency():
    tx = {"amount": 300}
    result = get_transaction_amount_in_rub(tx)
    assert result == 300.0
