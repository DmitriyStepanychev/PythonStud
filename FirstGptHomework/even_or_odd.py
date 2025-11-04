# Задача 6 (усложнённая): «Чётное или нечётное — с защитой от ошибок»
# Условие:
# Попроси пользователя ввести число.
# Если пользователь ввёл не число (например, букву или слово), программа должна вывести сообщение об ошибке и попросить ввести число снова.
# Когда введено корректное число, программа проверяет, чётное оно или нечётное, и выводит соответствующее сообщение.

# number = input('Please enter a number: ')
#
# while True:
#     try:
#         number = int(number)
#         break
#     except ValueError:
#         number = input('Ошибка: нужно ввести число!:')
#
# if number % 2 == 0:
#    print('Even')
# else:
#     print('Odd')

while True:
    number = input('Please enter a number: ')
    try:
        number = int(number)
        break
    except ValueError:
        print('Ошибка: нужно ввести число!')

if number % 2 == 0:
    print('Even')
else:
    print('Odd')
