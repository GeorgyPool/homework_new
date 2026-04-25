from src.decorators import log


# Проверка, что при отсутствии аргумента в декораторе, вывод выводится в консоль
def test_correct_in_consol(capsys):
    @log()
    def addition_numbers(x, y):
        return x + y

    result = addition_numbers(1, 2)
    print(result)
    captured = capsys.readouterr()
    assert captured.out == "addition_numbers ok, результат:3\n"


# Проверка, что при отсутствии аргумента в декораторе, вывод выводится в консоль
def test_correct_invalid_in_consol(capsys):
    @log()
    def addition_numbers(x, y):
        return x + y

    result = addition_numbers(1)
    print(result)
    captured = capsys.readouterr()
    assert captured.out == "addition_numbers error: TypeError. Inputs: (1,), {}\n"


# Проверяет что при передаче аргумента в декораторе создается файл с записью о работе функции
def test_correct_write_in_file(tmp_path):
    file = tmp_path / "test_write.txt"

    @log(str(file))
    def addition_numbers(x, y):
        return x + y

    result = addition_numbers(1, 2)

    assert file.is_file()

    with open(file, "r") as text:
        content = text.read()

    assert content == "addition_numbers ok, результат: 3"
