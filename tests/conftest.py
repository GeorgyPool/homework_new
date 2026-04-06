import pytest

#фикстуры для masks.py
#для функции get_mask_card_number
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

#для функции get_mask_account
@pytest.fixture
def account_number_short():
    return 73654108430


@pytest.fixture
def account_number_long():
    return 7565483847373782882737848995587