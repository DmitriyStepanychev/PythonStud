# Попроси пользователя ввести дату в формате YYYY-MM-DD (например, 2023-05-10).
# Выведи, сколько дней прошло от введённой даты до сегодняшней даты.
# Подсказка: используй datetime.date.today() и datetime.datetime.strptime.

import datetime

def date_time_input(prompt):
    while True:
        try:
            input_date = datetime.datetime.strptime(input(prompt), '%Y-%m-%d').date()
            return input_date
        except ValueError:
            print("Invalid date, try again. Example: 2024-02-15")

current_date = datetime.datetime.now().date()

input_date = date_time_input("Enter a date in format YYYY-MM-DD: ")

different_date = (current_date - input_date).days

print(f"С введенной даты {input_date} до сегодняшнего дня {current_date} прошло {different_date} дней")