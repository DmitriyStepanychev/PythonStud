# Создай функцию is_palindrome(word) → bool.
# Если слово читается одинаково слева направо и справа налево (например, “level”), возвращай True.

def is_palindrome(world)-> bool:
    if world == world[::-1]:
        return True
    else:
        return False

world = str(input("Input a word: "))
print(is_palindrome(world))

# def is_palindrome(word) -> bool:
#     cleaned = ''.join(ch.lower() for ch in word if ch.isalnum())
#     return cleaned == cleaned[::-1]