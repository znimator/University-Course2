def binary_search(numbers, key):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == key:
            return mid  # Элемент найден
        elif numbers[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Элемент не найден

def find_insert_position(numbers, key):
    left, right = 0, len(numbers)
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left

def main():
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    key = 10

    # Бинарный поиск
    index = binary_search(numbers, key)
    if index != -1:
        print(f"Число {key} найдено в позиции {index}.")
    else:
        print(f"Число {key} не найдено.")

    # Поиск позиции для вставки
    insert_pos = find_insert_position(numbers, key)
    print(f"Число {key} должно быть вставлено в позицию {insert_pos} для сохранения порядка.")

if __name__ == "__main__":
    main()