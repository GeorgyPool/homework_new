import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для функции get_mask_card_number
def test_get_mask_card_number_split_str_numbers(split_str_numbers):
    assert get_mask_card_number(split_str_numbers) == "1234 45** **** 1234"


def test_get_mask_card_number_str_isalpha(str_isalpha):
    with pytest.raises(ValueError):
        get_mask_card_number(str_isalpha)


def test_get_mask_card_number_witch_short(short_numbers):
    assert get_mask_card_number(short_numbers) == "Не корректная длина номера карты"


def test_get_mask_card_number_witch_loong(loong_numbers):
    assert get_mask_card_number(loong_numbers) == "Не корректная длина номера карты"


@pytest.mark.parametrize(
    "start_numbers, expected",
    [
        (1234567890123456, "1234 56** **** 3456"),
        (3564326784536784, "3564 32** **** 6784"),
        ("2456 5325322354 43", "2456 53** **** 5443"),
    ],
)
def test_of_correct_card_number_witch_loong(start_numbers, expected):
    assert get_mask_card_number(start_numbers) == expected


# Тесты для функции get_mask_account
@pytest.mark.parametrize(
    "start_number, expected", [(73654108430135874305, "**4305"), (73654108430135876890, "**6890")]
)
def test_get_mask_account(start_number, expected):
    assert get_mask_account(start_number) == expected


def test_get_mask_account_short_number(account_number_short):
    assert get_mask_account(account_number_short) == "Не корректная длина номера счета"


def test_get_mask_account_long_number(account_number_long):
    assert get_mask_account(account_number_long) == "Не корректная длина номера счета"
