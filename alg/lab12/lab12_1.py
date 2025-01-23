import hashlib

def compute_hash(file_path, hash_algo='sha256'):
    """Вычисляет хэш-сумму для файла."""
    hash_func = hashlib.new(hash_algo)
    print(f"[DEBUG] Открываем файл {file_path} для вычисления хэш-суммы.")
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            print(f"[DEBUG] Читаем блок данных размером {len(chunk)} байт.")
            hash_func.update(chunk)
    hash_value = hash_func.hexdigest()
    print(f"[DEBUG] Вычисленная хэш-сумма: {hash_value}")
    return hash_value

def append_hash(file_path, hash_value):
    """Добавляет хэш-сумму в конец файла."""
    print(f"[DEBUG] Открываем файл {file_path} для добавления хэш-суммы.")
    with open(file_path, 'a', newline='\n') as f:  # Гарантируем использование только '\n'
        f.write(f'\n{hash_value.strip()}')  # Удаляем лишние символы, если они есть
    print(f"[DEBUG] Хэш-сумма {hash_value} добавлена в конец файла.")

def main():
    input_file = 'input.txt'  # Файл, для которого вычисляется хэш-сумма

    # Показываем содержимое файла перед вычислением
    print(f"[DEBUG] Открываем файл {input_file} для проверки содержимого.")
    with open(input_file, 'rb') as f:
        file_data = f.read()
        print(f"[DEBUG] Содержимое файла (raw): {file_data}")
        try:
            print(f"[DEBUG] Содержимое файла (decoded): {file_data.decode('utf-8')}")
        except UnicodeDecodeError:
            print("[DEBUG] Ошибка декодирования содержимого файла.")

    # Вычисляем хэш-сумму
    hash_value = compute_hash(input_file)
    
    # Добавляем хэш-сумму в файл
    append_hash(input_file, hash_value)

    # Проверяем содержимое файла после добавления
    print(f"[DEBUG] Открываем файл {input_file} для проверки содержимого после добавления хэш-суммы.")
    with open(input_file, 'rb') as f:
        updated_file_data = f.read()
        print(f"[DEBUG] Содержимое файла (raw): {updated_file_data}")
        try:
            print(f"[DEBUG] Содержимое файла (decoded): {updated_file_data.decode('utf-8')}")
        except UnicodeDecodeError:
            print("[DEBUG] Ошибка декодирования содержимого файла.")

    print(f"Хэш-сумма {hash_value} добавлена в конец файла {input_file}.")

if __name__ == "__main__":
    main()
