# Попроси пользователя ввести число N
# и выведи сумму всех чётных чисел от 1 до N включительно.

while True:
    try:
        user_number = int(input("Input a number: "))
        even_sum = 0
        for i in range(0, user_number + 1):
            if i % 2 == 0:
                even_sum += i
        print(f"Sum of even numbers up to {user_number}: {even_sum}")
        break
    except ValueError:
        print("Invalid input, please input a number.")