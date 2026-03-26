def filter_by_state(list_of_dict, state_key="EXECUTED") -> list[dict]:
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
        "CANCELED",
    )
)


def sort_by_date(list_of_dict, key_data=True):
    if key_data == True:
      sorted_list = sorted(list_of_dict, key=lambda x: x['date'], reverse=True)
      return sorted_list
    else:
        sorted_list = sorted(list_of_dict, key=lambda x: x['date'])
        return sorted_list


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
))
