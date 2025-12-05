# Сгенерируй двухмерный список (матрицу) 10×10, где элемент [i][j] = (i+1) * (j+1) с помощью list comprehension.
# Выведи красиво первые 5 строк матрицы.

matrix = [[(i+1) * (j+1) for i in range(10)]for j in range(10)]

for i in range(5):
    for j in range(10):
        print(f"{matrix[i][j]:3}", end=' ')
    print()