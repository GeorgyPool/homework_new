import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import corrected_info_for_filter_by_currency


# Тест на корректность вывода генератора сортировки по заданному значению
def test_filter_by_currency(corrected_info_for_filter_by_currency):
    done = filter_by_currency(corrected_info_for_filter_by_currency, "USD")
    assert next(done) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(done) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

#тест на вывод при отсутствии ключа "code" в словаре
#при отсутствии ключа пропускает словарь
def test_dont_have_key_in_list(dot_have_key_in_list):
    done = filter_by_currency(dot_have_key_in_list)
    assert next(done) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    assert next(done) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }

# тест функции transaction_descriptions на положительный результат
def test_corrected_result_transaction_descriptions(corrected_info_for_filter_by_currency):
  done = transaction_descriptions(corrected_info_for_filter_by_currency)
  assert next(done) == "Перевод организации"
  assert next(done) == "Перевод со счета на счет"
  assert next(done) == "Перевод со счета на счет"
  assert next(done) == "Перевод с карты на карту"
  assert next(done) == "Перевод организации"

#тест на вызов ошибки при передачах пустого списка
def test_empty_list_transaction_descriptions():
    # Создаём итератор
    iterator = transaction_descriptions([])
    # Ловим исключение при попытке итерации
    with pytest.raises(ValueError):
        next(iterator)

#тесты для функции card_number_generator
@pytest.mark.parametrize("a, b, c, d", [(1, 2, "0000 0000 0000 0001", "0000 0000 0000 0002")])
def test_card_number_generator(a, b , c, d):
    done = card_number_generator(a, b)
    assert next(done) == c
    assert next(done) == d

#тест на вызов ошибки при передачах на положительного числа
def test_card_number_generator_invalid():
    iters = card_number_generator(0)
    with pytest.raises(ValueError):
        next(iters)

#тест на поднятие ошибки при передаче слишком большого числа
def test_card_number_generator_invalid_two():
    iters = card_number_generator(1, 99999999999999999)
    with pytest.raises(ValueError):
        next(iters)
