# Создай список товаров (например, ["хлеб", "молоко", "сыр"]).
# Позволь пользователю добавлять элементы, пока он не введёт пустую строку.
# В конце выведи:
# количество товаров,
# отсортированный список.

food_list = ["хлеб", "молоко", "сыр"]

while True:
    add_food = input(str("Add a food: "))

    if add_food:
        food_list.append(add_food)
    else:
        break

print(len(food_list))
print(sorted(food_list))