import pandas as pd


def read_to_csv(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""

    df = pd.read_csv(path, sep=";", encoding="utf-8")
    to_list_dict = df.to_dict(orient="records")

    return to_list_dict


def read_to_xl(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""

    df = pd.read_excel(path)
    to_list_dict = df.to_dict(orient="records")

    return to_list_dict


# if __name__ == "__main__":
#     print(read_to_csv("../data/transactions.csv"))
#     print(read_to_xl("../data/transactions_excel.xlsx"))
