import pytest

from src.processing import filter_by_state, sort_by_date


# тесты для функции filter_by_state
# тест сортировки по ключу по умолчанию
def test_filter_by_state(create_list):
    assert filter_by_state(create_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# тест сортировки по заданному ключу
def test_filter_by_state_witch_key(create_list):
    assert filter_by_state(create_list, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# тест сортировки при отсутствии ключа "state"
def test_filter_by_state_fail_state(create_list_fail):
    assert filter_by_state(create_list_fail) == []


@pytest.mark.parametrize("key_exe, key_can", [("EXECUTED", "CANCELED")])
def test_filter_by_state_witch_key_parametrize(key_exe, key_can, create_list):
    assert filter_by_state(create_list, key_exe) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(create_list, key_can) == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# тесты для функции sort_by_date
# тест правильной сортировки функции по убыванию даты
def test_sort_by_date_default(create_list, create_correct_sorted_list_default):
    assert sort_by_date(create_list) == create_correct_sorted_list_default


# тест сортировки по возрастанию
def test_sorted_by_date_key_data_false(create_list, create_correct_sorted_list_false):
    assert sort_by_date(create_list, False) == create_correct_sorted_list_false


# тест сортировки при одинаковых датах
def test_sorted_by_date_copy_date(create_copy_list, answer_by_create_copy_list):
    assert sort_by_date(create_copy_list) == answer_by_create_copy_list


def test_not_standard_date(create_not_standard_list):
    assert sort_by_date(create_not_standard_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06"},
        {"id": 939719570, "state": "EXECUTED", "date": "2015-06"},
    ]
