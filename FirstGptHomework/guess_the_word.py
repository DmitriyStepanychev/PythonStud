# Создай игру, где программа хранит секретное слово "python".
# Пользователь вводит слова, пока не угадает.
# Используй while True и break.


secret_world = "python"

while True:
    user_world = input("Please, input a world: ")
    if user_world.lower() == secret_world.lower():
        print("You guessed it")
        break
    else:
        print("Try again!")