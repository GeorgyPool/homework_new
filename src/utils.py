import json


def return_list_json_file(path: str) -> list[dict]:
    """Преобразует json файл в список транзакций"""

    # если файл не найден или пустой возвращает пустой список
    try:
        # если файл существует преобразовать его в список python
        with open(path, "r", encoding="utf-8") as file:
            list_operations = json.load(file)
            if isinstance(list_operations, list):
                return list_operations
            else:
                return []
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


if __name__ == "__main__":
    a = return_list_json_file("../data/operations.json")
    print(a)
