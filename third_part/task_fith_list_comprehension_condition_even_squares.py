# Создай список квадратов всех чётных чисел от 1 до N включительно
# (N вводит пользователь) с помощью одного выражения list comprehension.


def safe_input(prompt):
    while True:
        try:
            input_n = int(input(prompt))
            if input_n > 0:
                return input_n
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input, please enter a number")

n = safe_input("Enter a number: ")
new_list = [x ** 2 for x in range(1, n + 1) if x % 2 == 0]

print(f"Список квадратов всех четных чисел от 1 до N = {new_list}")