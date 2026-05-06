from unittest.mock import patch

from src.utils import return_list_json_file


# тест на открытие и использования json
@patch("builtins.open")
@patch("src.utils.json.load")
def test_patch_return_list_json_file(mock_json, mock_open):
    mock_json.return_value = [{"amount": 100, "id": 1}]
    mock_open.return_value.__enter__.return_value = mock_open
    assert return_list_json_file("tests.json") == [{"amount": 100, "id": 1}]
    mock_json.assert_called_once()


# тест при отсутствии файла в пути аргументе выводит пустой список
def test_not_file_return_list_json_file():
    assert return_list_json_file("../data/tests.json") == []


# тест при отсутствии списка внутри json файла выводит пустой список
def test_not_list_return_list_json_file():
    assert return_list_json_file("tests_json_file/tests_json_not_list.json") == []
