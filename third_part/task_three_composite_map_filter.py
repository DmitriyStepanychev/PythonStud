# Пользователь вводит список слов.
# Сначала отфильтруй слова длиной > 3, затем с помощью map сделай все слова в нижний регистр и выведи результат как список.


input_list = input("Enter a list of world separated by commas (press Enter to finish): ")

long_list = list(filter(lambda word: len(word.strip()) > 3, input_list.split(',')))
lower_case_list = list(map(lambda world: world.strip().lower(), long_list))

print(lower_case_list)