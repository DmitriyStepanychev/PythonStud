# Создай функцию calculate(a, b, operation), где:
# operation может быть "+", "-", "*", "/",
# функция возвращает результат,
# программа просит пользователя ввести два числа и операцию,
# выводит результат.
# Пример:
# Введите первое число: 8
# Введите второе число: 2
# Введите операцию: /
# Результат: 4.0


def calculate(a, b, operation):
    if operation == "+":
        operation_result = a + b
    elif operation == "-":
        operation_result = a - b
    elif operation == "*":
        operation_result = a * b
    elif operation == "/":
        operation_result = a / b
    else:
        print("Error: Incorrect operator entered")
    return operation_result

try:
    a = int(input("Please input number a: "))
except ValueError:
    print("Error: You must enter an integer!")

try:
    b = int(input("Please input number b: "))
except ValueError:
    print("Error: You must enter an integer!")

operation = input("Please input operation: ")

print(calculate(a, b, operation))


# Что можно улучшить:
# Если пользователь введёт неправильный оператор, в else: ты выводишь ошибку,
# но при этом operation_result не будет определён, и программа выдаст ошибку UnboundLocalError.
# → Лучше вернуть None или завершить выполнение в else через return.
# При делении можно добавить проверку деления на ноль.
# Чтобы не потерять контроль при вводе некорректных данных (a или b), лучше повторно запрашивать ввод в цикле, а не просто печатать ошибку.
# ✅ Улучшенная версия:
# def calculate(a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b
#     elif operation == "/":
#         if b == 0:
#             return "Error: Division by zero!"
#         return a / b
#     else:
#         return "Error: Invalid operator!"
#
#
# def get_number(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("Error: Please enter a valid number!")
#
#
# a = get_number("Please input number a: ")
# b = get_number("Please input number b: ")
# operation = input("Please input operation (+, -, *, /): ")
#
# print("Result:", calculate(a, b, operation))
#
#
# 💡 Что здесь улучшено:
# Обработка всех ошибок без падения программы.
# float, чтобы можно было вводить дробные числа.
# Код стал более читаемым и модульным.
