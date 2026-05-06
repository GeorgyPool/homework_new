# Банковское приложение:
приложение дня обработки данных банковских пользвателей

# Установка:
````
#в командной строке/терминале введите:
git clone git@github.com:GeorgyPool/homework_new.git
````
# Зависимости:
+ Python 3.14.3 - проект использует эту версию *python*

# Работа с модулями:
+ МОДУЛЬ [masks.py](src/masks.py) - обрабатывает номер счета/карты
и выдает маску данной информации:
````
#возврат маски номера карты
get_mask_card_number(7000792289606361) #7000 79** **** 6361

#возврат маски счета
get_mask_account(73654108430135874305) #**4305
````
+ МОДУЛЬ [widget.py](src/widget.py) - обрабатывает информацию 
как о картах, так и о счетах и дате:
````
#Возвращает строку с замаскированным номером для карт
и счетов
mask_account_card(Visa Platinum 7000792289606361)
mask_account_card(Счет 73654108430135874305) 
#Visa Platinum 7000 79** **** 6361
#Счет **4305

#возвращает строку с датой в формате ДД.ММ.ГГГГ
get_date("2024-03-11T02:26:18.671407") #("11.03.2024")
````
+ МОДУЛЬ [processing.py](src/processing.py) - сортировка информации 
по данным
````
#Функция возвращает список словарей 
только тех где ключ равен 'state_key'
filter_by_state(list_of_dict, state_key="EXECUTED")
#[{'id': 41428829, 'state': 'EXECUTED'}]

#Функция возвращающая отсортированый список 
словарей по дате по убыванию по умалчанию
sort_by_date(list_of_dict, key_data=True)
#[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
````

+ МОДУЛЬ [generators.py](src/generators.py) - содержит генераторы
````
#функция filter_by_currency принимает список словарей и 
возвращает итератор который выдает 
транзакции по заданной валюте

filter_by_currency(list[dict], find="USD")#выдаст все словари
из списка содержащие операции по "USD"

#функция transaction_descriptions принимает 
список словарей и возвращает итератор 
описания каждой операции по очереди

transaction_descriptions(list[dict])#"Перевод организации"

#функция card_number_generator принимает начальное и конечное 
значение для генерации номера банковских карт

card_number_generator(1, 2)#0000 0000 0000 0001
                           #0000 0000 0000 0002
 
````

+ МОДУЛЬ [decorators.py](src/decorators.py) - содержит декораторы
````
декоратор @log(): при отсутствии аргументов в декораторе выводи
логи в консоль, при передачи аргументов записывает логи в файл

@log("log.txt")
def func()      #запишит работу функции в файл с названием переданного аргумента
return
````
+ МОДУЛЬ [utils.py](src/utils.py) - содержит функционал для чтения json файлов и возвращает список python
````
#функия return_list_json_file():

#принимает путь до файла транзакций json
return_list_json_file("../data/operations.json") # [{operations}] список транзакций
````
+ МОДУЛЬ [external_api.py](src/external_api.py) - содержит функционал конвертации валюты
````
#Функция convert_currency():
#принимает словарь с информацией о транзакциях {transsctions}

convert_currency({transsctions}) #возвращает сумму, если сумма["amount"] указана в рублях["code"] == RUB
                                 #если сумма транзакции указана в EUR или USD обращается к API для конвертации
                                 #валюты и возвращает ее в рублях 
````

# Папка *tests* :
содержит тесты для модулей: 
+ [masks.py](src/masks.py)  - [test_masks.py](tests/test_masks.py)
+ [processing.py](src/processing.py) - [test_processing.py](tests/test_processing.py)
+ [widget.py](src/widget.py) - [test_widget.py](tests/test_widget.py)
+ [generators.py](src/generators.py) - [test_generators.py](tests/test_generators.py)
+ [decorators.py](src/decorators.py) - [test_decorators.py](tests/test_decorators.py)
+ [utils.py](src/utils.py) - [test_utils.py](tests/test_utils.py)
+ [external_api.py](src/external_api.py) - [test_external_api.py](tests/test_external_api.py)

модуль [conftest.py](tests/conftest.py): содержит данные для тестов

````
для запуска тестов в терменале пропишите комманду :

   pytest - запустит все тесты
   
   pytest tests/test_masks.py - запустит тест конкретного
   модуля
   
   pytest --cov - запустит тесты с 
   информацией о проценте покрытия
````
в папке [htmlcov](htmlcov) - [class_index.html](htmlcov/class_index.html) - содержится информация
о покрытии кода в html формате


# Папка *logs* :
````
содержит логи о выполнении модулей masks.py и utils.py
````