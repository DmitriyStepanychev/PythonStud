# Создай генератор square_numbers(n),
# который выдаёт квадраты чисел от 1 до n.
# Выведи результат в формате:
# 1² = 1
# 2² = 4
# 3² = 9

def safe_input(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a number: ")

def square_number(user_number):
    for i in range(1, user_number + 1):
        yield i ** 2


user_number = safe_input("Please enter a number: ")


print(f"Square numbers from 1 to {user_number}: ")
for num, square_num in enumerate(square_number(user_number), start=1):
    print(f"{num}² = {square_num}")