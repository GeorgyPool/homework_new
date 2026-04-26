def log(filename=None):
    """Декоратор записывающий лог в файл если передан
    аргумент filename, если аргумент не предан
    то выводит лог в консоль"""

    def log_inf(func):
        def wrapper(*args, **kwargs):
            # Если во время вызова основной функции возникает ошибка
            # То информация об ошибке записывается в лог
            try:
                result = func(*args, **kwargs)
                if isinstance(filename, str):
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok, результат: {result}")
                        return f"записано в лог файла {filename}"
                else:
                    return f"{func.__name__} ok, результат:{result}"
            except Exception as error:
                error_mes = f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}"
                if isinstance(filename, str):
                    with open(filename, "w") as file:
                        file.write(error_mes)
                    return f"записано в лог файла {filename}"
                else:
                    return error_mes

        return wrapper

    return log_inf


@log()
def my_func(x, y):
    return x + y


print(my_func(1))
