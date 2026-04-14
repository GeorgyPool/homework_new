from typing import Any

from src.masks import get_mask_account, get_mask_card_number  # type: ignore


def mask_account_card(bank_info: str) -> Any:
    """Возвращает строку с замаскированным номером для карт и счетов"""
    new_number_str = ""
    new_words_list = []

    # разделяет входные данные
    split_bank_info = bank_info.split()
    for index in split_bank_info:
        if index.isalpha():
            new_words_list.append(index)
        else:
            new_number_str += index

    # проверяет чтобы длина "Счета" всегда равнялась 20, в другом случае выбрасывает ошибку
    if "Счет" in new_words_list:
        if len(new_number_str) > 20 or len(new_number_str) < 20:
            raise ValueError("Не корректная длина счета")

    # проверяет чтобы длина номера банковской карты всегда равнялась 16, в другом случае выбрасывает ошибку
    if "Счет" not in new_words_list:
        if len(new_number_str) < 16 or len(new_number_str) > 16:
            raise ValueError("Не корректная длина номера банковской карты")

    # возвращает маску счета
    if "Счет" in new_words_list:
        if len(new_number_str) == 20:
            bank_account = get_mask_account(new_number_str)
            return f"{" ".join(new_words_list)} {bank_account}"

    # возвращает маску банковской карты
    elif len(new_number_str) == 16:
        bank_card = get_mask_card_number(new_number_str)
        return f"{" ".join(new_words_list)} {bank_card}"


def get_date(data: str) -> str:
    """Возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    split_data = data.split("-")

    # проверяет чтобы в дате обязательно было число, месяц, год
    if len(split_data) < 3:
        raise ValueError("Не корректная дата")

    # проверяет что длина число не меньше одной цифры
    for item in split_data:
        if len(item) < 1:
            raise ValueError("Не корректная дата")

    return f"{split_data[2][0:2]}.{split_data[1]}.{split_data[0]}"
