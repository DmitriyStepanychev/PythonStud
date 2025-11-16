# Создай функцию calculate(a, b, operation)
# и дай пользователю выбрать операцию (+, -, *, /).
# Выведи результат.
# ⚙️ Добавь проверку деления на ноль и некорректного ввода.


def calculate(a, b, operation):
    if operation == "+":
        return f"{a} + {b} = {a + b}"
    elif operation == "-":
        return f"{a} - {b} = {a - b}"
    elif operation == "*":
        return f"{a} * {b} = {a * b}"
    elif operation == "/":
        if b == 0:
            return "Division by zero"
        else:
            return f"{a} / {b} = {a / b}"
    else:
        return "Invalid operation"

def safe_input (input_number):
    try:
        return float(input(input_number))
    except ValueError:
        print("Invalid input, please input a number.")

a = safe_input("Input a number a: ")
b = safe_input("Input a number b: ")
operation = input("Input operation (+, -, *, /): ")

print(calculate(a, b, operation))