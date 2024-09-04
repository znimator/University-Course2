# Лаб 1. Задание 2. Вариант 8

# Дан массив действительных чисел. Среди них есть равные.
# Найдите его первый максимальный элемент и замените его нулем.

def replace_max_with_zero(arr):
    if not arr:
        return arr
    
    max_val = arr[0]
    max_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    
    arr[max_index] = 0
    return arr

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(replace_max_with_zero(A))
