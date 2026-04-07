import pytest

from src.widget import get_date, mask_account_card


# тесты для функции mask_account_card
@pytest.mark.parametrize(
    "start_info, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card_correct(start_info, expected):
    assert mask_account_card(start_info) == expected


def test_mask_account_witch_card(correct_masks_card):
    assert mask_account_card(correct_masks_card) == "MasterCard 7158 30** **** 6758"


def test_mask_account_card_witch_account(correct_masks_account):
    assert mask_account_card(correct_masks_account) == "Счет **4305"


def test_mask_account_card_invalid_witch_account():
    with pytest.raises(ValueError):
        assert mask_account_card("Счет 6468647367889477")


def test_mask_account_card_invalid_witch_card():
    with pytest.raises(ValueError):
        assert mask_account_card("visa Classic 683198247673765")


# тесты для функции get_date
@pytest.mark.parametrize(
    "start_info, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2026-03-11T02:26:18.671407", "11.03.2026"),
        ("2024-03-15T02:26:18.671407", "15.03.2024"),
        ("2024-01-11T02:26:18.671407", "11.01.2024"),
    ],
)
def test_get_date(start_info, expected):
    assert get_date(start_info) == expected


def test_get_date_invalid():
    with pytest.raises(ValueError):
        assert get_date("2024-03-")


def test_get_date_invalid_():
    with pytest.raises(ValueError):
        assert get_date("2024-03")
