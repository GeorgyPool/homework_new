from unittest.mock import patch

from src.external_api import convert_currency


# тест функция открывает request.get для запроса конвертации курса валют
@patch("requests.request")
def test_api_convert_currency(mock_get):
    mock_get.return_value.json.return_value = {"result": 1}
    assert convert_currency({"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}) == 1
    mock_get.assert_called_once()


# тест функции на корректную отдачу суммы если она указана в рублях
def test_currency_rub(currency_rub):
    assert convert_currency(currency_rub) == 31957.58
