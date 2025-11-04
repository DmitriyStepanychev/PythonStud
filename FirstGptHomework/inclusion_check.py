# Задача: “Проверка на вхождение”
# Попроси пользователя ввести слово.
# Проверь, есть ли это слово в строке "I love Python!".
# Выведи "Есть!" или "Нет!" в зависимости от результата.

world = input('Please enter a world: ')
text = 'I love Python!'
result = (f'{world}' in text)
if result:
    print('Есть!')
else:
    print('Нет!')

# Не нужно использовать f-строку внутри проверки, ведь world уже переменная:
# result = world in text
# Добавь регистронезависимость, чтобы “Love” и “love” считались одинаковыми:

world = input('Please enter a word: ')
text = 'I love Python!'
if world.lower() in text.lower():
    print('Есть!')
else:
    print('Нет!')