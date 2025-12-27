# Напиши декоратор repeat(n), который принимает число n и запускает обёрнутую функцию n раз.
# Декоратор должен собирать и возвращать список значений, возвращаемых каждой итерацией функции.
# Пример:
# @repeat(3)
# def f():
#     return random.randint(1, 10)
# # f() вернет [x1, x2, x3]

import random
from functools import wraps


def save_input(prompt):
    while True:
        try:
            input_n = int(input(prompt))
            if input_n >= 0:
                return input_n
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a positive integer number")


def repeat(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        n = save_input("Please enter a positive integer number how much function will be started: ")
        result = []
        for _ in range(n):
            result.append(func(*args, **kwargs))
        print(f"List of values for {func.__name__}: {result}")
        return result

    return wrapper


@repeat
def f():
    return random.randint(1, 10)

f()

# def repeat(n):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = []
#             for _ in range(n):
#                 result.append(func(*args, **kwargs))
#             return result
#         return wrapper
#     return decorator
#
#
# @repeat(3)
# def f():
#     return random.randint(1, 10)
#
#
# print(f())  # [7, 1, 4]
