from os.path import split


def get_mask_card_number(number_cart: int|str) -> str:
    """Функция возвращает маску номера банковской карты"""
    number_str = str(number_cart)
    split_number_str = number_str.split()
    join_str = "".join(split_number_str)

    if not join_str.isdigit():
        raise ValueError("Только цифры")

    if len(str(join_str)) < 16 or len(str(join_str)) > 16:
        return "Не корректная длина номера карты"

    return f"{join_str[:4]} {join_str[4:6]}** **** {join_str[-4:]}"


def get_mask_account(account_number: int|str) -> str:
    """Функция возвращает маску номера счета"""
    account_str = str(account_number)
    if len(account_str) < 20 or len(account_str) > 20:
        return "Не корректная длина номера счета"
    return f"**{account_str[-4:]}"
