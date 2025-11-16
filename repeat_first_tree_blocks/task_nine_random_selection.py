# Создай список из 5 имён и с помощью random.choice()
# выведи случайного победителя.
# ⚙️ Для продвинутого уровня — попроси ввести список имён вручную.

import random

name_list = []

while len(name_list) < 5:
    add_name = input("Enter at least five names: ")
    if add_name not in name_list:
        name_list.append(add_name)
    else:
        print('Name already in use')

print(f"Name list: {name_list}")
print(f"Random winner is {random.choice(name_list)}")