# Задача: “Покупки”
# Создай список товаров: ["молоко", "хлеб", "сыр"]
# Добавь ещё один товар, выведи длину списка и распечатай все элементы по одному через цикл for.

purchases = ['молоко', 'хлеб', 'сыр']

purchases.append('колбаса')

print(len(purchases))

for purchase in purchases:
    print(purchase)

# ⚙️ Что можно улучшить:
# Для улучшения читаемости вывода можно добавить поясняющие тексты:
#
# print(f'Количество покупок: {len(purchases)}')
# print('Список покупок:')
# for purchase in purchases:
#     print('-', purchase)
#
#
# Это делает результат более “дружелюбным”.
# Можно позволить пользователю добавить покупки самому:
#
# purchases = ['молоко', 'хлеб', 'сыр']
#
# while True:
#     item = input('Добавить товар (или нажмите Enter для выхода): ')
#     if not item:
#         break
#     purchases.append(item)
#
# print(f'\nВсего товаров: {len(purchases)}')
# for purchase in purchases:
#     print('-', purchase)