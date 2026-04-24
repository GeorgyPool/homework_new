def log(filename=None):
    def log_inf(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if isinstance(filename, str):
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    return f"{func.__name__} ok, результат:{result}"
            except Exception as error:
                error_mes = f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}"
                if isinstance(filename, str):
                    with open(filename, "w") as file:
                        file.write(error_mes)
                else:
                    return error_mes

        return wrapper

    return log_inf


@log("mylog.txt")
def my_func(x, y):
    return x + y


print(my_func(5, 9))
