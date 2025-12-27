# Сделай мини-утилиту «Анализ продаж»:
# Программа принимает от пользователя строки в формате имя,количество,цена до пустой строки (пример: Bread,10,1.5).
# Собери данные в список/словарь.
# С помощью list comprehension и map создайте список общих стоимостей для каждой позиции (количество * цена).
# Отфильтруйте позиции с общей стоимостью > X (значение X вводит пользователь).
# Выведите:
# общее число позиций,
# суммарную выручку,
# отсортированный по убыванию список позиций по общей стоимости.
# Добавь декоратор log_calls, который будет логировать (в консоль) дату/время и имя вызываемой функции при каждом вызове
# (используй datetime).
# Bread,10,1
# Aple,10,1.5
# Banana,10,2
# Eggs,10,3
# Potato,10,4
# Milk,10,5
# Orange,10,6
# Meat,10,10

from datetime import datetime
from functools import wraps



def log_calls(func):
    @wraps(func)
    def wrapper(*args):
        print(f"function {func.__name__} called at {datetime.now()}")
        return func(*args)

    return wrapper


@log_calls
def safe_input_item(prompt):
    item_list = []
    while True:
        item_str = input(prompt)

        if not item_str.strip():
            return None

        try:
            item_list = item_str.split(",")
            if len(item_list) != 3:
                print("Invalid input, enter 'name,quantity,price'")
            else:
                return item_list
        except ValueError:
            print("Please enter a correct data")


@log_calls
def safe_input_total_cost(prompt):
    while True:
        try:
            total_cost = float(input(prompt))
            return total_cost
        except ValueError:
            print("Please enter a float number")


@log_calls
def create_items_list():
    items_list = []
    while True:
        list_of_item = safe_input_item(
            "Please, enter 'name,quantity,price' separated by commas (press Enter to finish): ")
        if list_of_item is None:
            break
        else:
            items_list.append(list_of_item)
    return items_list


list_of_items = create_items_list()
print(list_of_items)  # для проверки ввода


@log_calls
def list_of_total_costs(list_of_items):
    name = [item[0] for item in list_of_items]
    quantity = [item[1] for item in list_of_items]
    price = [item[2] for item in list_of_items]
    list_of_total_costs = list(map(lambda q, p: float(q) * float(p), quantity, price))
    dict_of_total_costs = dict(zip(name, list_of_total_costs))
    return dict_of_total_costs


total_cost_dict = list_of_total_costs(list_of_items)

print(total_cost_dict)  # для проверки списка общих стоимостей


@log_calls
def filter_items_by_total_cost(total_cost_dict):
    user_total_costs = safe_input_total_cost(
        "Please enter the total price by which you would like to filter products.: ")
    filtered_items_by_total_cost_list = list(filter(lambda x: x > user_total_costs, total_cost_dict.values()))
    return filtered_items_by_total_cost_list


filtered_costs = filter_items_by_total_cost(total_cost_dict)
print(filtered_costs)  # для проверки фильтра списка общих стоимостей

print(f"Общее число позиций: {len(filtered_costs)}")

sum_total_cost_list = sum(float(x) for x in total_cost_dict.values())
print(f"Суммарная выручка: {sum_total_cost_list}")

sorted_cost_list = dict(sorted(total_cost_dict.items(), key=lambda x: x[1], reverse=True))
print(f"отсортированный по убыванию список позиций по общей стоимости: {sorted_cost_list}")
