import random

def maxValues(matrix):
    result = []
    for row in matrix:
        result.append(max(row))
    return result

def randomMatrix(rows, columns):
    matrix = []
    for _ in range(rows):
        matrix.append([random.randint(0, 100) for _ in range(columns)])
    return matrix

matrix = randomMatrix(5, 5)
print(matrix)
print(maxValues(matrix))