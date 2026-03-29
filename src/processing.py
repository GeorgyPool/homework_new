def filter_by_state(list_of_dict: list[dict], state_key: str = "EXECUTED") -> list[dict]:
    """Сортирует список словарей по ключу"""
    new_list_dict = []

    for index in list_of_dict:
        if index["state"] == state_key:
            new_list_dict.append(index)

    return new_list_dict


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "EXECUTED",
    )
)


def sort_by_date(list_of_dict: list[dict], key_data: bool = True) -> list[dict]:
    """Сортирует список словарей по дате (по убыванию)"""
    if key_data:
        sorted_list = sorted(list_of_dict, key=lambda x: x["date"], reverse=True)
        return sorted_list
    else:
        sorted_list = sorted(list_of_dict, key=lambda x: x["date"])
        return sorted_list


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
