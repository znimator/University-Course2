import numpy as np

def hourglass(n):
    matrix = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(i, n - i):
            matrix[i][j] = 1
            matrix[n - i - 1][j] = 1 

    return matrix

n = 5
hourglass_matrix = hourglass(n)
print(np.rot90(hourglass_matrix))