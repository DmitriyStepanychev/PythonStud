# Задача: “Мини-калькулятор”
# Считай два числа через input(), приведи их к float
# Выведи их сумму, разность, произведение и частное (всё в отдельных строках).

first_number = float(input('Please enter a first number: '))
second_number = float(input('Please enter a second number: '))

# print(first_number + second_number)
# print(first_number - second_number)
# print(first_number * second_number)
# print(first_number / second_number)

# Добавь пояснения к каждому результату — пользователю так будет понятнее:

print(f"Сумма: {first_number + second_number}")
print(f"Разность: {first_number - second_number}")
print(f"Произведение: {first_number * second_number}")
# print(f"Частное: {first_number / second_number}")

# Можно добавить проверку деления на ноль (для надёжности):

if second_number == 0:
    print("Ошибка: деление на ноль!")
else:
    print(f"Частное: {first_number / second_number}")