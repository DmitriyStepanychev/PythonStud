# Задача 10 (усложнённая): «Среднее значение списка чисел»
# Условие:
# Попроси пользователя ввести несколько чисел через запятую (например: 3, 7, 2, 9, 5).
# Твоя программа должна:
# Разделить введённую строку на отдельные элементы.
# Преобразовать их в числа (int или float).
# Вычислить среднее арифметическое.
# Если пользователь введёт нечисловое значение — вывести сообщение об ошибке и попросить повторить ввод.


while True:
    user_input = input('Please enter several numbers separated by commas: ')
    list_of_numbers = user_input.split(',')
    try:
        # Преобразуем все элементы списка в числа
        numbers = [float(num.strip()) for num in list_of_numbers]

        # Вычисляем среднее
        average = sum(numbers) / len(numbers)
        print(f'Average value: {average}')
        break
    except ValueError:
        print('Error: please enter numbers only!')