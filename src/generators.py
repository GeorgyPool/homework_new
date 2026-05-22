from typing import Generator, Iterator


def filter_by_currency(list_transactions: list[dict], find: str = "USD") -> Iterator[dict]:
    """Функция возвращающая итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""

    for trans in list_transactions:
        # проверяет есть ли ключ "code" в списке
        # при отсутствии ключа пропускает транзакцию
        if "operationAmount" in trans:
            if "code" in trans["operationAmount"]["currency"]:
                code = trans["operationAmount"]["currency"]["code"]
                if find == code:
                    yield trans
        elif "currency_code" in trans:
            code = trans["currency_code"]
            if find == code:
                yield trans
        else:
            continue


def transaction_descriptions(list_transactions: list[dict]) -> Iterator[dict]:
    """Возвращает итератор описания каждой операции по очереди"""
    # если список пустой поднимает ошибку пустой список
    if list_transactions:
        # возвращает описание транзакций по одной за раз
        for x in list_transactions:
            yield x["description"]
    else:
        raise ValueError("пустой список")


def card_number_generator(start: int = 1, stop: int = 9) -> Generator[str]:
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX
    от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    # проверяет чтобы начальное число было больше конечного
    # вызывает ошибку если start > stop
    if start > stop:
        raise ValueError("Начальное значение не может быть больше конечного")
    # проверяет чтобы начальное число было положительным, конечное число было меньше 999999999999999
    elif start <= 0 or stop > 9999999999999999:
        raise ValueError("""начальное значение должно быть положительным
        конечное значение не должно превышать 9999999999999999""")

    for num in range(start, stop + 1):
        s = f"{str(num).zfill(16)}"
        yield f"{s[:4]} {s[4:8]} {s[8:12]} {s[12:16]}"


# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
#     {
#         "id": 873106923,
#         "state": "EXECUTED",
#         "date": "2019-03-23T01:09:46.296404",
#         "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 44812258784861134719",
#         "to": "Счет 74489636417521191160",
#     },
#     {
#         "id": 895315941,
#         "state": "EXECUTED",
#         "date": "2018-08-19T04:27:37.904916",
#         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод с карты на карту",
#         "from": "Visa Classic 6831982476737658",
#         "to": "Visa Platinum 8990922113665229",
#     },
#     {
#         "id": 594226727,
#         "state": "CANCELED",
#         "date": "2018-09-12T21:27:25.241689",
#         "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Visa Platinum 1246377376343588",
#         "to": "Счет 14211924144426031657",
#     },
# ]


# if __name__ == "__main__":
#     usd_transactions = filter_by_currency(transactions, "USD")
#     for _ in range(2):
#         print(next(usd_transactions))

# if __name__ == "__main__":
#     descriptions = transaction_descriptions([])
#     for _ in range(5):
#         try:
#             print(next(descriptions))
#         except StopIteration as fail:
#             print("конец итерации")


# if __name__ == "__main__":
#     for card_number in card_number_generator(0, 9999):
#         print(card_number)

# if __name__ == "__main__":
#     info = card_number_generator(150, 99999)
#     with open("number_card", "w") as file:
#         for num in info:
#             file.write(num + "\n")
