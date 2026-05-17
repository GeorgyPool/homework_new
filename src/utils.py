import datetime
import json
import logging

today = datetime.datetime.today()
today_str = today.strftime("%Y-%m-%d")

# вызов библиотеки logging и установка уровня вывода сообщений
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# установка конфигурации логов
file_handler = logging.FileHandler(f"../logs/{today_str}-utils.log","w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s %(funcName)s: %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def return_list_json_file(path: str) -> list[dict]:
    """Преобразует json файл в список транзакций"""

    # если файл не найден или пустой возвращает пустой список
    try:
        logger.info("Открытие файла")
        # если файл существует преобразовать его в список python
        with open(path, "r", encoding="utf-8") as file:

            list_operations = json.load(file)

            if isinstance(list_operations, list):
                logger.info("Успешное преобразование JSON в список Python")
                return list_operations

            else:
                logger.error("JSON‑файл не содержит список")
                return []

    except FileNotFoundError as ex:
        logger.error(f"Ошибка: {ex}")
        return []

    except json.decoder.JSONDecodeError:
        logger.error("Ошибка: некорректный формат JSON")
        return []


if __name__ == "__main__":
    a = return_list_json_file("../data/operations.json")
    print(a)
