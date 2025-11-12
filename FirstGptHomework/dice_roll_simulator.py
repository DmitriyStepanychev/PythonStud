# Сделай программу, которая при каждом запуске выводит случайное число от 1 до 6.
#  Используй randint(1, 6)
#  Для красоты добавь функцию roll_dice().

import random

def roll_dice():
    roll = random.randint(1, 6)
    return roll

dice_result = roll_dice()
print(f"Rolled dice: {dice_result}")