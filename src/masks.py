def get_mask_card_number(number_cart: int) -> str:
    """Функция которая возвращает маску номера банковской карты"""
    number_str = str(number_cart)
    return f"{number_str[:4]} {number_str[4:6]}** **** {number_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """функция которая возвращает маску номера счета"""
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
