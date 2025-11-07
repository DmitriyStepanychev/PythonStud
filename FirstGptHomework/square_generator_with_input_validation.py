# Создай генераторную функцию square_numbers(n), которая выдаёт квадраты чисел от 1 до n включительно.
# Пользователь вводит число n.
# Если введено не число — программа должна вывести сообщение об ошибке и попросить ввести заново.
#
# После этого программа красиво выводит результат в формате:
#
# Квадраты чисел от 1 до 5:
# 1² = 1
# 2² = 4
# 3² = 9
# 4² = 16
# 5² = 25

def square_number(n):
    num = 1
    square_num = 1
    while num < n + 1:
        yield square_num ** 2
        num += 1
        square_num += 1

try:
    n = int(input("Input a number: "))
except ValueError:
    print("Error: You must enter a number!")

print(f"Square numbers from 1 to {n}: ")
for num, square_num in enumerate(square_number(n), start=1):
        print(f"{num}² = {square_num}")

# Что можно улучшить:
# Избыточные переменные
# Тебе не нужно отдельно хранить square_num и num — достаточно одной.
# Можно просто перебирать числа от 1 до n и yield i ** 2.
# Обработка ошибок
# Сейчас при некорректном вводе программа продолжит выполнение с необъявленной n.
# Лучше сделать цикл, чтобы просить ввод до тех пор, пока не получено число.
# Оптимизированная версия твоего кода:
# def square_numbers(n):
#     for i in range(1, n + 1):
#         yield i ** 2
#
#
# while True:
#     try:
#         n = int(input("Input a number: "))
#         if n > 0:
#             break
#         else:
#             print("Please enter a positive number!")
#     except ValueError:
#         print("Error: You must enter a number!")
#
# print(f"\nSquare numbers from 1 to {n}:")
# for num, square in enumerate(square_numbers(n), start=1):
#     print(f"{num}² = {square}")