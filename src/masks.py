import datetime
import logging

today = datetime.datetime.today()
today_str = today.strftime("%Y-%m-%d")

# вызов библиотеки logging и установка уровня вывода сообщений
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# установка конфигурации логов
file_handler = logging.FileHandler(f"../logs/{today_str}_masks.log","W", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s %(funcName)s: %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(number_cart: int | str) -> str:
    """Функция возвращает маску номера банковской карты"""

    logger.info("Вызов функции")

    number_str = str(number_cart)
    split_number_str = number_str.split()
    join_str = "".join(split_number_str)

    if not join_str.isdigit():
        logger.error("Введены не корректные символы")
        raise ValueError("Только цифры")

    if len(str(join_str)) < 16 or len(str(join_str)) > 16:
        logger.error("Не корректная длина номера карты")
        return "Не корректная длина номера карты"

    logger.info("Успешное завершение функции")
    return f"{join_str[:4]} {join_str[4:6]}** **** {join_str[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """Функция возвращает маску номера счета"""

    logger.info("Вызов функции")
    account_str = str(account_number)

    if len(account_str) < 20 or len(account_str) > 20:
        logger.error("Не корректная длина номера счета")
        return "Не корректная длина номера счета"

    logger.info("Успешное выполнение")
    return f"**{account_str[-4:]}"


print(get_mask_card_number("0000000000000000"))
print(get_mask_account("00000000000000000000"))
