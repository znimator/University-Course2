import random

def saddlePoint(matrix):
    n = len(matrix)
    result = None
    for i in range(n):
        min_row = min(matrix[i])
        for j in range(n):
            if matrix[i][j] == min_row and matrix[i][j] == max([matrix[k][j] for k in range(n)]):
                result = (i, j)
                break
    return result

def randomMatrix(rows, columns):
    matrix = []
    for _ in range(rows):
        matrix.append([random.randint(0, 100) for _ in range(columns)])
    return matrix

while True:
    matrix = randomMatrix(5, 5)
    print("Исходная:")
    for i, row in enumerate(matrix):
        print(i + 1, row)

    matrix = saddlePoint(matrix)

    print()
    print('После:')
    if matrix is None:
        print('Нет седловых точек')
    else:
        # Чтобы понятнее было, где находится, а то от 0 считать не удобно
        print(matrix[0] + 1, matrix[1] + 1)
        break
