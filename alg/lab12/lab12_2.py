import hashlib

def compute_hash(data, hash_algo='sha256'):
    """Вычисляет хэш-сумму для переданных данных."""
    hash_func = hashlib.new(hash_algo)
    hash_func.update(data)
    return hash_func.hexdigest()

def get_file_data_without_last_line(file_path):
    """Читает данные из файла и разделяет их на данные без последней строки и саму последнюю строку."""
    with open(file_path, 'rb') as f:
        data = f.read()

    print(f"[DEBUG] Полный размер файла: {len(data)} байт")
    print(f"[DEBUG] Содержимое файла (raw): {data}")

    if len(data) == 0:
        print("[DEBUG] Файл пуст.")
        return b'', b''

    # Ищем последнюю строку
    if data.endswith(b'\n'):
        last_newline = data.rfind(b'\n', 0, -1)
    else:
        last_newline = data.rfind(b'\n')

    if last_newline == -1:
        print("[DEBUG] Символы новой строки не найдены.")
        return data, b''

    # Убираем лишние символы \r
    data_without_last_line = data[:last_newline].replace(b'\r', b'')
    last_line = data[last_newline + 1:].strip()

    print(f"[DEBUG] Данные без последней строки (raw): {data_without_last_line}")
    print(f"[DEBUG] Последняя строка (raw): {last_line}")
    return data_without_last_line, last_line

def main():
    input_file = 'input.txt'  # Файл, для которого проверяется хэш-сумма

    # Читаем данные файла
    data_without_last_line, last_line = get_file_data_without_last_line(input_file)

    if not last_line:
        print("[DEBUG] Контрольная хэш-сумма не найдена в файле.")
        return

    # Декодируем последнюю строку
    try:
        stored_hash = last_line.decode('utf-8').strip()
        print(f"[DEBUG] Контрольная хэш-сумма из файла (decoded): {stored_hash}")
    except UnicodeDecodeError:
        print("[DEBUG] Ошибка декодирования контрольной хэш-суммы.")
        return

    # Вычисляем хэш-сумму для данных без последней строки
    computed_hash = compute_hash(data_without_last_line)
    print(f"[DEBUG] Вычисленная хэш-сумма: {computed_hash}")

    # Сравниваем хэш-суммы
    if computed_hash == stored_hash:
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
