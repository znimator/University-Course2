import random

__all__ = [
    'maxValues',
    'randomMatrix',
]

def maxValues(matrix):
    """Return a list of maximum values from each row of the matrix."""
    return [max(row) for row in matrix]

def randomMatrix(rows, columns):
    """Return a matrix of random integers."""
    return [[random.randint(0, 100) for _ in range(columns)] for _ in range(rows)]
