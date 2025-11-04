# Задача: “Магическая строка”
# Создай строку text = "Python"
# Умножь её на 3 и выведи результат.
# Добавь к ней " is cool" и выведи снова.

text = 'Python'
result = text * 3
print(result)
print(f'{result} is cool')

text = 'Python '
result = text * 3
print(result.strip())  # уберёт лишний пробел в конце
print(f'{result.strip()} is cool')
