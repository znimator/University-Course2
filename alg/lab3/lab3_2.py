import random

def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def randomMatrix(rows, columns):
    matrix = []
    for _ in range(rows):
        matrix.append([random.randint(0, 100) for _ in range(columns)])
    return matrix


matrix = [[0,1,1],[1,0,1],[1,1,0]]
for i, row in enumerate(matrix):
    print(i + 1, row)

print(is_symmetric(matrix))