# Напиши декоратор timeit, который измеряет и печатает время выполнения обёрнутой функции (в секундах).
# Проверь декоратор на функции, которая генерирует список из 1_000_000 случайных чисел (используй random) и сортирует его.

# 1) Функция генератор, который генерирует список из 1_000_000 случайных чисел.
# 2) Декоратор timeit, который считает время выполнения функции

import random
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        spent_time = end - start
        print(f"Function {func.__name__} took {spent_time:.6f} seconds")
        return result

    return wrapper

@timeit
def list_generator(size = 1_000_000):
    random_numbers = [random.random() for _ in range(size)]
    random_numbers.sort()
    return random_numbers

result = list_generator()
# print(f"Result: {result}")
print(f"Min: {result[0]}, Max: {result[-1]}")