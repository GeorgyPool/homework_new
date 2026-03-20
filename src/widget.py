from masks import get_mask_account, get_mask_card_number  # type: ignore


def mask_account_card(bank_info: str) -> str:
    """Возвращает строку с замаскированным номером для карт и счетов"""
    new_number_str = ""
    new_words_list = []

    split_bank_info = bank_info.split()
    for index in split_bank_info:
        if index.isalpha():
            new_words_list.append(index)
        else:
            new_number_str += index

    if len(new_number_str) > 16:
        bank_account = get_mask_account(new_number_str)
        return f"{" ".join(new_words_list)} {bank_account}"
    else:
        bank_card = get_mask_card_number(new_number_str)
        return f"{" ".join(new_words_list)} {bank_card}"


def get_date(data: str) -> str:
    """возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    split_data = data.split("-")

    return f"{split_data[2][0:2]}.{split_data[1]}.{split_data[0]}"
