import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей (data) и строку поиска, возвращает список словарей
    у которых в описании (data: x["description"]) есть совпадение со строкой поиска (search)"""

    find_match = [
        x
        for x in data
        if "description" in x and x["description"] is not None and re.search(search, str(x["description"]), re.I)
    ]

    return find_match


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с транзакциями, и список категорий,
    возвращает словарь с количеством упоминаний в каждой категории"""

    # Оставляем только те словари, где есть совпадение по строкам из categories в description
    list_categories = [x for x in data if "description" in x and x["description"] in categories]
    # Подсчитываем общее количество каждой категории
    count_categories = Counter(x["description"] for x in list_categories)

    return count_categories
