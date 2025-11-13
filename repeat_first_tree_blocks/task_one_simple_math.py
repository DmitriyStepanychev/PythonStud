# 🔹 1. Простая математика.
# Попроси пользователя ввести два числа.
# Выведи:
# сумму,
# разность,
# произведение,
# частное (если возможно).
# ⚙️ Проверь деление на ноль.



try:
    user_number_one = int(input("Please, input the first number: "))
    user_number_two = int(input("Please, input the second number: "))

    if user_number_two == 0:
        print("Error: Division by zero!")
    else:
        print(f"Sum: {user_number_one + user_number_two}")
        print(f"Product: {user_number_one * user_number_two}")
        print(f"Difference: {user_number_one - user_number_two}")
        print(f"Division: {user_number_one / user_number_two}")

except ValueError:
    print("Invalid input, please input a number.")

# компактная “профессиональная” версия:
# def safe_input(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("Please enter a valid number.")
#
# a = safe_input("Enter first number: ")
# b = safe_input("Enter second number: ")
#
# if b == 0:
#     print("Error: Division by zero!")
# else:
#     print(f"Sum: {a + b}\nDifference: {a - b}\nProduct: {a * b}\nDivision: {a / b:.2f}")
