# Компьютер загадывает число от 1 до 20.
# Пользователь вводит попытки, пока не угадает.
# После угадывания программа выводит:
# Вы угадали число за X попыток!

import random


def compare_function(user_number, guessed_number, attempts):
    if user_number == guessed_number:
        print(f"You guessed the number in {attempts} attempts!")
        return True
    elif user_number > guessed_number:
        print(f"{user_number} is to HIGH, your attempts for now is {attempts}, try again")
        return False
    else:
        print(f"{user_number} is to LOW, your attempts for now is {attempts}, try again")
        return False


guessed_number = random.randint(1, 20)
attempts = 0

while True:
    print("Enter a 'q' to quit")
    user_input = input("Please enter a number: ")

    if user_input.lower() == "q":
        print("Thank you for playing!")
        break

    try:
        user_number = int(user_input)
        attempts += 1
        if compare_function(user_number, guessed_number, attempts):
            break
    except ValueError:
        print("Invalid input, please input a number")