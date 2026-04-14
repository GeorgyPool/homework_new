import pytest


# Фикстуры для masks.py
# для функции get_mask_card_number
@pytest.fixture
def split_str_numbers():
    return "1234 4564 7894 1234"


@pytest.fixture
def short_numbers():
    return 675803848576487


@pytest.fixture
def loong_numbers():
    return 6758038485764878473628394


@pytest.fixture
def str_isalpha():
    return "hello bany hou are you"


# для функции get_mask_account
@pytest.fixture
def account_number_short():
    return 73654108430


@pytest.fixture
def account_number_long():
    return 7565483847373782882737848995587


# Фикстуры для модуля widget.py
# для функции mask_account_card
@pytest.fixture
def correct_masks_card():
    return "MasterCard 7158300734726758"


@pytest.fixture
def correct_masks_account():
    return "Счет 73654108430135874305"


# Фикстуры для модуля processing.py
# для функции filter_by_state
@pytest.fixture
def create_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# списки без ключа "state"
@pytest.fixture
def create_list_fail():
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


# для функции sort_by_date
@pytest.fixture
def create_correct_sorted_list_default():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def create_correct_sorted_list_false():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# повторяющиеся даты 2 и 3
@pytest.fixture
def create_copy_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# ответ для фикстуры выше
@pytest.fixture
def answer_by_create_copy_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]


# не стандартный ключ date
@pytest.fixture
def create_not_standard_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2015-06"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
