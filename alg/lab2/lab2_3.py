import random

def maxMod(matrix):
    max_mod = 0
    max_mod_i = 0
    max_mod_j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            mod = abs(matrix[i][j])
            if mod > max_mod:
                max_mod = mod
                max_mod_i = i
                max_mod_j = j
    return max_mod, max_mod_i, max_mod_j

def swapRows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

def swapCols(matrix, i, j):
    for row in matrix:
        row[i], row[j] = row[j], row[i]

def moveToK(matrix, k):
    max_mod, max_mod_i, max_mod_j = maxMod(matrix)
    swapRows(matrix, max_mod_i, k-1)
    swapCols(matrix, max_mod_j, k-1)

def randomMatrix(rows, columns):
    matrix = []
    for _ in range(rows):
        matrix.append([random.randint(0, 100) for _ in range(columns)])
    return matrix

matrix = randomMatrix(5, 5)
k = 3

print("Исходная:")
for i, row in enumerate(matrix):
    print(i + 1, row)

moveToK(matrix, k)

print()
print(f'После (K = {k}):')

for i, row in enumerate(matrix):
    print(i + 1, row)
