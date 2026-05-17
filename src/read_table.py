import pandas as pd


def read_to_csv(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""

    # Проверка на ошибки
    try:
        df = pd.read_csv(path, sep=";", encoding="utf-8")
        # Если файл пустой, то выдает пустой список словарей
        if df.empty:
            return [{}]
        # Если все верно, возвращает список словарей
        to_list_dict = df.to_dict(orient="records")
        return to_list_dict

    except FileNotFoundError:
        print(f"Файл: {path} не найден")
    except Exception as ex:
        print(f"Произошла ошибка: {type(ex)}")


def read_to_xl(path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""

    # Проверка на ошибки
    try:
        df = pd.read_excel(path)
        # Если файл пустой, то выдает пустой список словарей
        if df.empty:
            return [{}]
        # Если все верно, возвращает список словарей
        to_list_dict = df.to_dict(orient="records")
        return to_list_dict

    except FileNotFoundError:
        print(f"Файл: {path} не найден")
    except Exception as ex:
        print(f"Произошла ошибка: {type(ex)}")


# if __name__ == "__main__":
#     print(read_to_csv("../data/transactions.csv"))
#     print(read_to_xl("../data/transactions_excel.xlsx"))
