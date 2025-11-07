# Создай генератор random_numbers(count, start, end),
# который возвращает заданное количество случайных чисел в диапазоне [start, end].

import random

start = int(input("Please input start number: "))
end = int(input("Please input end number: "))
count = int(input("Please input count: "))


def random_number(count, start, end):
    number = 1
    while number <= count:
        yield random.randrange(start, end + 1)
        number += 1


print(list(random_number(count, start, end)))

# import random
#
# def random_numbers(count, start, end):
#     """Генератор случайных чисел в диапазоне [start, end]"""
#     for _ in range(count):
#         yield random.randint(start, end)
#
#
# while True:
#     try:
#         start = int(input("Please input start number: "))
#         end = int(input("Please input end number: "))
#         count = int(input("Please input count: "))
#
#         if start >= end:
#             print("Error: start must be less than end!")
#             continue
#         if count <= 0:
#             print("Error: count must be a positive number!")
#             continue
#         break
#     except ValueError:
#         print("Error: please enter valid integers!")
#
# print(f"\nRandom {count} numbers from {start} to {end}:")
# for num in random_numbers(count, start, end):
#     print(num)

