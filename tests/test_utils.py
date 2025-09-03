import pytest
from src.utils import load_transactions_from_json
import os
import json

def test_load_correct_json(tmp_path):
    data = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
    file = tmp_path / "transactions.json"
    file.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions_from_json(str(file))
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == 1

def test_load_empty_file(tmp_path):
    file = tmp_path / "empty.json"
    file.write_text("", encoding="utf-8")

    result = load_transactions_from_json(str(file))
    assert result == []

def test_load_non_list_json(tmp_path):
    file = tmp_path / "not_list.json"
    file.write_text(json.dumps({"key": "value"}), encoding="utf-8")

    result = load_transactions_from_json(str(file))
    assert result == []

def test_load_file_not_found():
    result = load_transactions_from_json("non_existent_file.json")
    assert result == []
