from unittest.mock import patch

import pandas
import pytest

from src.read_table import read_to_csv, read_to_xl


# Тесты read_to_csv
def tests_read_to_csv_is_positive():
    with patch("pandas.read_csv") as mock_read:
        mock_read.return_value = pandas.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        result = read_to_csv("data.csv")
        expected = [{"col1": 1, "col2": 3}, {"col1": 2, "col2": 4}]
        assert result == expected
        mock_read.assert_called_once_with("data.csv", sep=";", encoding="utf-8")


def tests_read_to_csv_is_empty():
    with patch("pandas.read_csv") as mock_read:
        mock_read.return_value = pandas.DataFrame([])
        result = read_to_csv("data.csv")
        expected = [{}]
        assert result == expected
        mock_read.assert_called_once_with("data.csv", sep=";", encoding="utf-8")


def test_read_to_csv_not_file():
    with patch("builtins.print") as mock_print:
        result = read_to_csv("tests.csv")
        assert result is None
        mock_print.assert_called_once_with("Файл: tests.csv не найден")


def tests_read_to_csv_invalid():
    with pytest.raises(Exception):
        result = read_to_csv("tests.csv")
        assert result == "Файл: tests.csv не найден"


# тесты read_to_xl
def tests_read_to_xl_is_positive():
    with patch("pandas.read_excel") as mock_pd:
        mock_pd.return_value = pandas.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        result = read_to_xl("tests.xlsx")
        expected = [{"col1": 1, "col2": 3}, {"col1": 2, "col2": 4}]
        assert result == expected
        mock_pd.assert_called_once_with("tests.xlsx")


def test_read_to_xl_is_empty():
    with patch("pandas.read_excel") as mock_pd:
        mock_pd.return_value = pandas.DataFrame([])
        result = read_to_xl("tests.xlsx")
        assert result == [{}]
        mock_pd.assert_called_once_with("tests.xlsx")


def test_read_to_xl_not_file():
    with patch("builtins.print") as mock_print:
        result = read_to_xl("tests.xlsx")
        assert result is None
        mock_print.assert_called_once_with("Файл: tests.xlsx не найден")


def test_read_to_xl_invalid():
    with pytest.raises(Exception):
        result = read_to_xl("tests.xlsx")
        assert result == "Файл: tests.xlsx не найден"
