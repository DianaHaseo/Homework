import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize("items, state, expected", [
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "PENDING"},
            {"id": 3, "state": "EXECUTED"},
        ],
        "EXECUTED",
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 3, "state": "EXECUTED"},
        ],
    ),
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "PENDING"},
            {"id": 3, "state": "CANCELLED"},
        ],
        "PENDING",
        [
            {"id": 2, "state": "PENDING"},
        ],
    ),
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "EXECUTED"},
        ],
        "CANCELLED",
        [],
    ),
    (
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 2},  # без ключа 'state'
            {"id": 3, "state": "EXECUTED"},
        ],
        "EXECUTED",
        [
            {"id": 1, "state": "EXECUTED"},
            {"id": 3, "state": "EXECUTED"},
        ],
    ),
    (
        [],
        "EXECUTED",
        [],
    ),
])
def test_filter_by_state(items, state, expected):
    assert filter_by_state(items, state) == expected

def test_filter_by_state_default():
    items = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"},
        {"id": 3, "state": "EXECUTED"},
    ]
    expected = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    assert filter_by_state(items) == expected

    import pytest
    from src.processing import sort_by_date  # замените your_module на имя вашего модуля

    @pytest.mark.parametrize("items, descending, expected_dates", [
        (
                [
                    {"id": 1, "date": "2023-06-29"},
                    {"id": 2, "date": "2022-01-01"},
                    {"id": 3, "date": "2023-06-28"},
                ],
                True,
                ["2023-06-29", "2023-06-28", "2022-01-01"],
        ),
        (
                [
                    {"id": 1, "date": "2023-06-29"},
                    {"id": 2, "date": "2022-01-01"},
                    {"id": 3, "date": "2023-06-28"},
                ],
                False,
                ["2022-01-01", "2023-06-28", "2023-06-29"],
        ),
        (
                [
                    {"id": 1, "date": "2023-06-29"},
                    {"id": 2, "date": "2023-06-29"},
                    {"id": 3, "date": "2023-06-28"},
                ],
                True,
                ["2023-06-29", "2023-06-29", "2023-06-28"],
        ),
    ])
    def test_sort_by_date(items, descending, expected_dates):
        sorted_items = sort_by_date(items, descending)
        result_dates = [item['date'] for item in sorted_items]
        assert result_dates == expected_dates

    @pytest.mark.parametrize("items", [
        [{"id": 1, "date": "29-06-2023"}],  # неправильный формат
        [{"id": 2, "date": "2023/06/29"}],  # неправильный формат
        [{"id": 3, "date": "invalid-date"}],  # невалидная дата
        [{"id": 4, "date": ""}],  # пустая строка
    ])
    def test_sort_by_date_invalid_format(items):
        with pytest.raises(ValueError):
            sort_by_date(items)