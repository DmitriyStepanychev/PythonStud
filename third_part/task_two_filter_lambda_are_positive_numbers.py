# Дан список чисел (ввод пользователя через запятую).
# Отфильтруй только положительные числа с помощью filter и lambda и выведи их.

list_of_numbers = []

while True:
    number_input = input("Please, enter numbers separated by commas (press Enter to finish): ")

    if not number_input:
        break

    try:
        # сначала проверяем весь ввод
        nums = [float(x) for x in number_input.split(",")]
        # если всё хорошо — добавляем в общий список
        list_of_numbers.extend(nums)
    except ValueError:
        print("Invalid input, please enter numbers only!")

# фильтрация положительных чисел
new_list_of_numbers = list(filter(lambda x: x > 0, list_of_numbers))
print(new_list_of_numbers)
