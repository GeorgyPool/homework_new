import os.path

from src.read_table import read_to_csv, read_to_xl
from src.utils import return_list_json_file
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.widget import mask_account_card, get_date
from src.search import process_bank_operations, process_bank_search

text = """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""

operation_list = ["EXECUTED", "CANCELED", "PENDING"]


def main():
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")
    user_input = int(input("Введите выбор: "))

    if user_input == 1:
        print("Для обработки выбран JSON-файл")
        print(text)
        while True:
            user_filter = input("Введите фильтрацию: ").upper()

            if user_filter in operation_list:
                # фильтрация по статусу
                filter_state_result = filter_by_state(return_list_json_file(os.path.join("data", "operations.json")), user_filter)
                user_input_data = input("Отсортировать операции по дате? Да/Нет").lower()

                if user_input_data == "нет":
                    user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").lower()

                    if user_input_currency == "нет":
                        user_input_sort_by_words = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()

                        if user_input_sort_by_words == "нет":
                            # список категорий
                            list_description = [x["description"] for x in filter_state_result if "description" in x]
                            result_count = process_bank_operations(filter_state_result, list_description)
                            print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                            for x in filter_state_result:
                                if "from" in x:
                                    print(f"{get_date(x['date'])} {x['description']}")
                                    print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                    print(f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")

                        elif user_input_sort_by_words == "да":
                            user_input_word = input("Введите слово для выборки")
                            result_words_search = process_bank_search(filter_state_result, user_input_word)
                            if result_words_search:
                                list_description = [x["description"] for x in result_words_search if "description" in x]
                                result_count = process_bank_operations(result_words_search, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_words_search:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                        print(f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")

                            else:
                                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

                    elif user_input_currency == "да":
                        list_by_rub = list(filter_by_currency(filter_state_result, "RUB"))
                        user_input_sort_by_words = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                        if user_input_sort_by_words == "нет":
                            list_description = [x["description"] for x in list_by_rub if "description" in x]
                            result_count = process_bank_operations(list_by_rub,list_description)
                            print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                            for x in list_by_rub:
                                if "from" in x:
                                    print(f"{get_date(x['date'])} {x['description']}")
                                    print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                    print(
                                        f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")
                        elif user_input_sort_by_words == "да":
                            user_input_word = input("Введите слово для выборки")
                            result_search = process_bank_search(list_by_rub, user_input_word)
                            if result_search:
                                list_description = [x["description"] for x in result_search if "description" in x]
                                result_count = process_bank_operations(result_search, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_search:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                        print(f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")
                            else:
                                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                elif user_input_data == "да":
                    user_inpt_sort_data = input("Отсортировать по возрастанию или по убыванию?").lower()

                    if user_inpt_sort_data == "по возрастанию":
                        result_sort_bu_date = sort_by_date(filter_state_result, False)
                        user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").lower()

                        if user_input_currency == "нет":
                            user_input_by_words = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()

                            if user_input_by_words == "нет":
                                list_description = [x["description"] for x in result_sort_bu_date if "description" in x]
                                result_count = process_bank_operations(result_sort_bu_date, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_sort_bu_date:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                        print(f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")
                            elif user_input_by_words == "да":
                                user_input_search = input("Введите слово для выборки")
                                result_search = process_bank_search(result_sort_bu_date,user_input_search)
                                if result_search:
                                    list_description = [x["description"] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if "from" in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                            print(
                                                f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")
                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                        elif user_input_currency == "да":
                            result_by_rub = list(filter_by_currency(result_sort_bu_date, "RUB"))
                            user_input_search = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
                            if user_input_search == "нет":
                                list_description = [x["description"] for x in result_by_rub if "description" in x]
                                result_count = process_bank_operations(result_by_rub, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_by_rub:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                        print(f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")
                            elif user_input_search == "да":
                                user_input_word = input("Введите слово для выборки").lower()
                                result_search = process_bank_search(result_by_rub, user_input_word)
                                if result_search:
                                    list_description = [x["description"] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if "from" in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                            print(f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")

                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


                    elif user_inpt_sort_data == "по убыванию":
                        result_sort_bu_date = sort_by_date(filter_state_result)
                        user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").lower()
                        if user_input_currency == "нет":
                            user_input_search = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
                            if user_input_search == "нет":
                                list_description = [x["description"] for x in result_sort_bu_date if "description" in x]
                                result_count = process_bank_operations(result_sort_bu_date, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_sort_bu_date:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                        print( f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")
                            elif user_input_search == "да":
                                user_input_word = input("Введите слово для выборки").lower()
                                result_search = process_bank_search(result_sort_bu_date, user_input_word)
                                if result_search:
                                    list_description = [x["description"] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if "from" in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                            print(f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")
                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                        elif user_input_currency == "да":
                            result_by_rub = list(filter_by_currency(result_sort_bu_date, "RUB"))
                            user_input_search = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
                            if user_input_search == "нет":
                                list_description = [x["description"] for x in result_by_rub if "description" in x]
                                result_count = process_bank_operations(result_by_rub, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_by_rub:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                        print(f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")
                            elif user_input_search == "да":
                                user_input_word = input("Введите слово для выборки").lower()
                                result_search = process_bank_search(result_by_rub, user_input_word)
                                if result_search:
                                    list_description = [x['description'] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if 'from' in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(f"{mask_account_card(x['from'])} -> {mask_account_card(x['to'])}")
                                            print(f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")
                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

                break
            elif user_filter not in operation_list:
                print(f"Статус операции '{user_filter}' недоступен.")
                print(text)

    elif user_input == 2:
        print("Для обработки выбран CSV-файл")
        print(text)
        while True:
            user_filter = input("Введите фильтрацию: ").upper()

            if user_filter in operation_list:
                # фильтрация по статусу
                filter_state_result = filter_by_state(read_to_csv(os.path.join("data", "transactions.csv")),
                                                      user_filter)
                user_input_data = input("Отсортировать операции по дате? Да/Нет").lower()

                if user_input_data == "нет":
                    user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").lower()

                    if user_input_currency == "нет":
                        user_input_sort_by_words = input(
                            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()

                        if user_input_sort_by_words == "нет":
                            # список категорий
                            list_description = [x["description"] for x in filter_state_result if "description" in x]
                            result_count = process_bank_operations(filter_state_result, list_description)
                            print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                            for x in filter_state_result:
                                if "from" in x:
                                    print(f"{get_date(x['date'])} {x['description']}")
                                    print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                    print(f"{x['amount']} {x['currency_name']}\n")

                        elif user_input_sort_by_words == "да":
                            user_input_word = input("Введите слово для выборки")
                            result_words_search = process_bank_search(filter_state_result, user_input_word)
                            if result_words_search:
                                list_description = [x["description"] for x in result_words_search if "description" in x]
                                result_count = process_bank_operations(result_words_search, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_words_search:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")

                            else:
                                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

                    elif user_input_currency == "да":
                        list_by_rub = list(filter_by_currency(filter_state_result, "RUB"))
                        user_input_sort_by_words = input(
                            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                        if user_input_sort_by_words == "нет":
                            list_description = [x["description"] for x in list_by_rub if "description" in x]
                            result_count = process_bank_operations(list_by_rub, list_description)
                            print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                            for x in list_by_rub:
                                if "from" in x:
                                    print(f"{get_date(x['date'])} {x['description']}")
                                    print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                    print(f"{x['amount']} {x['currency_name']}\n")
                        elif user_input_sort_by_words == "да":
                            user_input_word = input("Введите слово для выборки")
                            result_search = process_bank_search(list_by_rub, user_input_word)
                            if result_search:
                                list_description = [x["description"] for x in result_search if "description" in x]
                                result_count = process_bank_operations(result_search, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_search:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            else:
                                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                elif user_input_data == "да":
                    user_inpt_sort_data = input("Отсортировать по возрастанию или по убыванию?").lower()

                    if user_inpt_sort_data == "по возрастанию":
                        result_sort_bu_date = sort_by_date(filter_state_result, False)
                        user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").lower()

                        if user_input_currency == "нет":
                            user_input_by_words = input(
                                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()

                            if user_input_by_words == "нет":
                                list_description = [x["description"] for x in result_sort_bu_date if "description" in x]
                                result_count = process_bank_operations(result_sort_bu_date, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_sort_bu_date:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            elif user_input_by_words == "да":
                                user_input_search = input("Введите слово для выборки")
                                result_search = process_bank_search(result_sort_bu_date, user_input_search)
                                if result_search:
                                    list_description = [x["description"] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if "from" in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(
                                                f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                            print(f"{x['amount']} {x['currency_name']}\n")
                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                        elif user_input_currency == "да":
                            result_by_rub = list(filter_by_currency(result_sort_bu_date, "RUB"))
                            user_input_search = input(
                                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
                            if user_input_search == "нет":
                                list_description = [x["description"] for x in result_by_rub if "description" in x]
                                result_count = process_bank_operations(result_by_rub, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_by_rub:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            elif user_input_search == "да":
                                user_input_word = input("Введите слово для выборки").lower()
                                result_search = process_bank_search(result_by_rub, user_input_word)
                                if result_search:
                                    list_description = [x["description"] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if "from" in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(
                                                f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                            print(f"{x['amount']} {x['currency_name']}\n")

                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


                    elif user_inpt_sort_data == "по убыванию":
                        result_sort_bu_date = sort_by_date(filter_state_result)
                        user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").lower()
                        if user_input_currency == "нет":
                            user_input_search = input(
                                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
                            if user_input_search == "нет":
                                list_description = [x["description"] for x in result_sort_bu_date if "description" in x]
                                result_count = process_bank_operations(result_sort_bu_date, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_sort_bu_date:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            elif user_input_search == "да":
                                user_input_word = input("Введите слово для выборки").lower()
                                result_search = process_bank_search(result_sort_bu_date, user_input_word)
                                if result_search:
                                    list_description = [x["description"] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if "from" in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(
                                                f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                            print(f"{x['amount']} {x['currency_name']}\n")
                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                        elif user_input_currency == "да":
                            result_by_rub = list(filter_by_currency(result_sort_bu_date, "RUB"))
                            user_input_search = input(
                                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
                            if user_input_search == "нет":
                                list_description = [x["description"] for x in result_by_rub if "description" in x]
                                result_count = process_bank_operations(result_by_rub, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_by_rub:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            elif user_input_search == "да":
                                user_input_word = input("Введите слово для выборки").lower()
                                result_search = process_bank_search(result_by_rub, user_input_word)
                                if result_search:
                                    list_description = [x['description'] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if 'from' in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(
                                                f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                            print(f"{x['amount']} {x['currency_name']}\n")
                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

                break
    elif user_input == 3:
        print("Для обработки выбран XLSX-файл")
        print(text)
        while True:
            user_filter = input("Введите фильтрацию: ").upper()

            if user_filter in operation_list:
                # фильтрация по статусу
                filter_state_result = filter_by_state(read_to_xl(os.path.join("data", "transactions_excel.xlsx")),
                                                      user_filter)
                user_input_data = input("Отсортировать операции по дате? Да/Нет").lower()

                if user_input_data == "нет":
                    user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").lower()

                    if user_input_currency == "нет":
                        user_input_sort_by_words = input(
                            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()

                        if user_input_sort_by_words == "нет":
                            # список категорий
                            list_description = [x["description"] for x in filter_state_result if "description" in x]
                            result_count = process_bank_operations(filter_state_result, list_description)
                            print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                            for x in filter_state_result:
                                if "from" in x:
                                    print(f"{get_date(x['date'])} {x['description']}")
                                    print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                    print(f"{x['amount']} {x['currency_name']}\n")

                        elif user_input_sort_by_words == "да":
                            user_input_word = input("Введите слово для выборки")
                            result_words_search = process_bank_search(filter_state_result, user_input_word)
                            if result_words_search:
                                list_description = [x["description"] for x in result_words_search if "description" in x]
                                result_count = process_bank_operations(result_words_search, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_words_search:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")

                            else:
                                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

                    elif user_input_currency == "да":
                        list_by_rub = list(filter_by_currency(filter_state_result, "RUB"))
                        user_input_sort_by_words = input(
                            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
                        if user_input_sort_by_words == "нет":
                            list_description = [x["description"] for x in list_by_rub if "description" in x]
                            result_count = process_bank_operations(list_by_rub, list_description)
                            print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                            for x in list_by_rub:
                                if "from" in x:
                                    print(f"{get_date(x['date'])} {x['description']}")
                                    print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                    print(f"{x['amount']} {x['currency_name']}\n")
                        elif user_input_sort_by_words == "да":
                            user_input_word = input("Введите слово для выборки")
                            result_search = process_bank_search(list_by_rub, user_input_word)
                            if result_search:
                                list_description = [x["description"] for x in result_search if "description" in x]
                                result_count = process_bank_operations(result_search, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_search:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            else:
                                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                elif user_input_data == "да":
                    user_inpt_sort_data = input("Отсортировать по возрастанию или по убыванию?").lower()

                    if user_inpt_sort_data == "по возрастанию":
                        result_sort_bu_date = sort_by_date(filter_state_result, False)
                        user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").lower()

                        if user_input_currency == "нет":
                            user_input_by_words = input(
                                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()

                            if user_input_by_words == "нет":
                                list_description = [x["description"] for x in result_sort_bu_date if "description" in x]
                                result_count = process_bank_operations(result_sort_bu_date, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_sort_bu_date:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            elif user_input_by_words == "да":
                                user_input_search = input("Введите слово для выборки")
                                result_search = process_bank_search(result_sort_bu_date, user_input_search)
                                if result_search:
                                    list_description = [x["description"] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if "from" in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(
                                                f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                            print(f"{x['amount']} {x['currency_name']}\n")
                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                        elif user_input_currency == "да":
                            result_by_rub = list(filter_by_currency(result_sort_bu_date, "RUB"))
                            user_input_search = input(
                                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
                            if user_input_search == "нет":
                                list_description = [x["description"] for x in result_by_rub if "description" in x]
                                result_count = process_bank_operations(result_by_rub, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_by_rub:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            elif user_input_search == "да":
                                user_input_word = input("Введите слово для выборки").lower()
                                result_search = process_bank_search(result_by_rub, user_input_word)
                                if result_search:
                                    list_description = [x["description"] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if "from" in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(
                                                f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                            print(f"{x['amount']} {x['currency_name']}\n")

                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


                    elif user_inpt_sort_data == "по убыванию":
                        result_sort_bu_date = sort_by_date(filter_state_result)
                        user_input_currency = input("Выводить только рублевые транзакции? Да/Нет").lower()
                        if user_input_currency == "нет":
                            user_input_search = input(
                                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
                            if user_input_search == "нет":
                                list_description = [x["description"] for x in result_sort_bu_date if "description" in x]
                                result_count = process_bank_operations(result_sort_bu_date, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_sort_bu_date:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            elif user_input_search == "да":
                                user_input_word = input("Введите слово для выборки").lower()
                                result_search = process_bank_search(result_sort_bu_date, user_input_word)
                                if result_search:
                                    list_description = [x["description"] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if "from" in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(
                                                f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                            print(f"{x['amount']} {x['currency_name']}\n")
                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
                        elif user_input_currency == "да":
                            result_by_rub = list(filter_by_currency(result_sort_bu_date, "RUB"))
                            user_input_search = input(
                                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower()
                            if user_input_search == "нет":
                                list_description = [x["description"] for x in result_by_rub if "description" in x]
                                result_count = process_bank_operations(result_by_rub, list_description)
                                print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                for x in result_by_rub:
                                    if "from" in x:
                                        print(f"{get_date(x['date'])} {x['description']}")
                                        print(f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                        print(f"{x['amount']} {x['currency_name']}\n")
                            elif user_input_search == "да":
                                user_input_word = input("Введите слово для выборки").lower()
                                result_search = process_bank_search(result_by_rub, user_input_word)
                                if result_search:
                                    list_description = [x['description'] for x in result_search if "description" in x]
                                    result_count = process_bank_operations(result_search, list_description)
                                    print(f"\nВсего банковских операций в выборке: {sum(result_count.values())}\n")
                                    for x in result_search:
                                        if 'from' in x:
                                            print(f"{get_date(x['date'])} {x['description']}")
                                            print(
                                                f"{mask_account_card(str(x['from']))} -> {mask_account_card(x['to'])}")
                                            print(f"{x['amount']} {x['currency_name']}\n")
                                else:
                                    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

                break



if __name__ == "__main__":
    main()