import random

def averageOfMatrix(matrix):
    min_val = float('inf')
    max_val = float('-inf')

    for row in matrix:
        for val in row:
            min_val = min(min_val, val)
            max_val = max(max_val, val)

    return (min_val + max_val) / 2

def randomMatrix(rows, columns):
    matrix = []
    for _ in range(rows):
        matrix.append([random.randint(0, 100) for _ in range(columns)])
    return matrix

matrix = randomMatrix(5, 5)
print(matrix)
print(averageOfMatrix(matrix))
