# Попроси пользователя ввести число N.
# Выведи сумму всех чётных чисел от 1 до N включительно.


user_number = int(input("Please input a nubber N: "))

total =0
for i in range(1, user_number + 1):
    if i % 2 == 0:
        total += i
print("Sum of even numbers is: ", total)


# то же самое можно сделать в одну строку
# n = int(input("Please input a number N: "))
# print("Sum of even numbers is:", sum(i for i in range(1, n + 1) if i % 2 == 0))
