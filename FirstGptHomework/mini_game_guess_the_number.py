# Мини-игра: “Угадай число”
# Функциональные требования:
# Программа загадывает случайное число от 1 до 20.
# Пользователь вводит свои догадки.
# Если число меньше или больше загаданного — программа подсказывает.
# После угадывания выводится количество попыток.
from platformdirs import user_runtime_dir


# что надо реализовать:
# функция guessed_number :randint(1,20)
# сравнение user_number и guessed_number
# счетчик попыток

import random

def compare_function(attempts):

    if user_number == guessed_number:
         print(f'You guessed the number in {attempts} attempts')
    elif user_number > guessed_number:
        print('You entered too large a value, try again')
    else:
        print('You entered too small value, try again')


guessed_number = random.randint(1, 20)
attempts = 1

while True:
    print('Enter "q" for exit: ')
    user_number = input('Enter your number: ')

    if user_number == "q":
        print('Thank you for playing')
        break
    try:
        user_number = int(user_number)
        compare_function(attempts)
        attempts += 1
    except ValueError:
        print('Invalid input, please input a number')


# Что можно улучшить:
# Область видимости переменных:
# В функции compare_function(attempts) ты используешь user_number и guessed_number,
# но они определены вне функции — это работает, но лучше передавать их как аргументы.
# После угадывания числа (user_number == guessed_number)
# программа должна заканчиваться, а сейчас она продолжает спрашивать.
# Нужно добавить return True и проверять это в основном цикле.
# Логичнее увеличивать attempts в начале каждой попытки, чтобы первая была “№1”.
# ✅ Исправленный и улучшенный вариант:
# import random
#
# def compare_function(user_number, guessed_number, attempts):
#     if user_number == guessed_number:
#         print(f'🎉 You guessed the number in {attempts} attempts!')
#         return True
#     elif user_number > guessed_number:
#         print('Too high! Try again.')
#     else:
#         print('Too low! Try again.')
#     return False
#
#
# guessed_number = random.randint(1, 20)
# attempts = 0
#
# while True:
#     print('Enter "q" to quit.')
#     user_input = input('Enter your number: ')
#
#     if user_input.lower() == "q":
#         print('Thanks for playing!')
#         break
#
#     try:
#         user_number = int(user_input)
#         attempts += 1
#         if compare_function(user_number, guessed_number, attempts):
#             break
#     except ValueError:
#         print('Invalid input, please enter a number.')
#
# 💡 Что улучшено:
# ✅ Передача аргументов в функцию явно — чистый код без зависимостей.
# ✅ Игра корректно завершается при угадывании.
# ✅ Логика с подсказками и счётчиком выстроена правильно.
# ✅ Улучшен текст для пользователя.