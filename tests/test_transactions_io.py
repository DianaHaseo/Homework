from unittest.mock import MagicMock, mock_open, patch

from src.transactions_io import read_transactions_from_csv, read_transactions_from_excel


def test_read_transactions_from_csv():
    csv_content = "id,amount,currency\n1,100,RUB\n2,200,USD\n"
    with patch("builtins.open", mock_open(read_data=csv_content)):
        result = read_transactions_from_csv("dummy.csv")
    assert isinstance(result, list)
    assert result[0]['id'] == '1'
    assert result[1]['currency'] == 'USD'


@patch("openpyxl.load_workbook")
def test_read_transactions_from_excel(mock_load_workbook):
    mock_wb = MagicMock()
    mock_sheet = MagicMock()
    mock_sheet.iter_rows.return_value = iter([
        [MagicMock(value='id'), MagicMock(value='amount'), MagicMock(value='currency')],
        [1, 100, 'RUB'],
        [2, 200, 'USD'],
    ])
    mock_wb.active = mock_sheet
    mock_load_workbook.return_value = mock_wb

    result = read_transactions_from_excel("dummy.xlsx")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]['id'] == 1
    assert result[1]['currency'] == 'USD'
