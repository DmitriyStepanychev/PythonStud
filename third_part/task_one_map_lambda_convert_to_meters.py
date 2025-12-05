# Пользователь вводит список расстояний в километрах, например: 3, 5.5, 10.
# Напиши программу, которая с помощью map и lambda преобразует каждый элемент в метры и выводит список метров.
# Подсказка: meters = list(map(lambda x: x * 1000, km_list))

km_list = []

while True:
    km_input = input("Please, enter km value (press Enter to finish): ")

    if not km_input:
        break

    try:
        km_list.append(float(km_input))
    except ValueError:
        print("Invalid input, please enter a number!")

meters_list = list(map(lambda x: x * 1000, km_list))
print(meters_list)