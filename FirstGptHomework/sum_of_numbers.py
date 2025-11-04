# Задача: “Сумма чисел от 1 до N”
# Введи N.
# С помощью for посчитай сумму чисел от 1 до N.
# Выведи результат.

sum = 0
n = int(input('Please input a number N: '))
for i in range(1, n + 1):
    sum += i
print(sum)

# ⚙️ Что можно улучшить:
# Не стоит использовать имя переменной sum, так как оно перекрывает встроенную функцию sum() в Python.
# Лучше назвать, например, total или result.
# Для более “питоничного” подхода можно решить задачу одной строкой, используя встроенную функцию:

n = int(input('Please input a number N: '))
total = sum(range(1, n + 1))
print(total)

# (Дополнительно) Можно добавить обработку ошибок, если пользователь введёт не число:

try:
    n = int(input('Please input a number N: '))
    print(sum(range(1, n + 1)))
except ValueError:
    print('Ошибка: нужно ввести целое число!')