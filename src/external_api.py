import os
from os import getenv

import requests
from dotenv import load_dotenv


def convert_currency(transactions: dict) -> float:
    """Конвертирует валюту в рубли если она в USD EUR и т.д
    Если валюта в рублях то выводит сумму 'amount'"""

    if transactions["operationAmount"]["currency"]["code"] == "RUB":
        return float(transactions["operationAmount"]["amount"])

    else:
        first_c = transactions["operationAmount"]["currency"]["code"]
        amount_c = transactions["operationAmount"]["amount"]

        load_dotenv()
        head = {"apikey": os.getenv("API_KEY")}
        url = f"https://api.apilayer.com/exchangerates_data/convert"
        payload = {"amount": amount_c, "from": first_c, "to": "RUB"}

        response = requests.request("GET", url, headers=head, params=payload)
        return float(response.json()["result"])


if __name__ == "__main__":
    a = convert_currency(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
    b = convert_currency(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )
    print(a)
    print(b)
