def filter_by_state(list_of_dict: list[dict], state_key: str = "EXECUTED") -> list[dict]:
    """Сортирует список словарей по ключу"""
    new_list_dict = []

    for index in list_of_dict:
        if index["state"] == state_key:
            new_list_dict.append(index)

    return new_list_dict


def sort_by_date(list_of_dict: list[dict], key_data: bool = True) -> list[dict]:
    """Сортирует список словарей по дате (по убыванию)"""
    if key_data:
        sorted_list = sorted(list_of_dict, key=lambda x: x["date"], reverse=True)
        return sorted_list
    else:
        sorted_list = sorted(list_of_dict, key=lambda x: x["date"])
        return sorted_list
