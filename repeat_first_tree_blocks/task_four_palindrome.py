# Создай функцию is_palindrome(text),
# которая возвращает True, если строка читается одинаково в обе стороны
# (без учёта регистра и пробелов).

def is_palindrome(text):
    cleaned_text = ''.join(world.lower() for world in text if world.isalnum())
    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False

text = str(input("Input a text: "))
print(is_palindrome(text))
