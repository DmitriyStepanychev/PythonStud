# Попроси пользователя ввести предложение.
# Выведи:
# количество символов,
# количество пробелов,
# строку в верхнем и нижнем регистре.

user_string = input("Please input a string: ")

print("number of characters: ", len(user_string))
print("number of spaces: ", user_string.count(" "))
print("Uppercase version:", user_string.upper())
print("Lowercase version:", user_string.lower())