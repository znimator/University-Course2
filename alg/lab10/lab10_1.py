def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:")
    print(arr)

    sorted_arr = bubble_sort(arr.copy())
    print("\nBubble Sort:")
    print(sorted_arr)

    sorted_arr = insertion_sort(arr.copy())
    print("\nInsertion Sort:")
    print(sorted_arr)

    sorted_arr = selection_sort(arr.copy())
    print("\nSelection Sort:")
    print(sorted_arr)

    sorted_arr = quick_sort(arr.copy())
    print("\nQuick Sort:")
    print(sorted_arr)
