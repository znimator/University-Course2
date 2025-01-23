def read_numbers(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
    return numbers

def write_result(filename, result):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(result))

def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1

def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    input_file = 'input_numbers.txt'
    output_file_linear = 'output_linear_search.txt'
    output_file_binary = 'output_binary_search.txt'
    target = 42  # Число, которое мы ищем

    # Чтение чисел из файла
    numbers = read_numbers(input_file)
    if not numbers:
        print("Файл пуст или содержит некорректные данные.")
        return

    # Линейный поиск
    index_linear = linear_search(numbers, target)
    if index_linear != -1:
        result_linear = f"Число {target} найдено в позиции {index_linear} (линейный поиск)."
    else:
        result_linear = f"Число {target} не найдено (линейный поиск)."
    write_result(output_file_linear, result_linear)

    # Бинарный поиск
    index_binary = binary_search(numbers, target)
    if index_binary != -1:
        result_binary = f"Число {target} найдено в позиции {index_binary} (бинарный поиск)."
    else:
        result_binary = f"Число {target} не найдено (бинарный поиск)."
    write_result(output_file_binary, result_binary)

    print("Поиск завершен. Результаты записаны в файлы.")

if __name__ == "__main__":
    main()