def check_brackets(text):
    """
    Проверяет соответствие открывающих и закрывающих скобок в тексте.

    Параметры:
    text (str): Текст, в котором нужно проверить скобки.

    Возвращает:
    bool: True, если скобки соответствуют, иначе False.
    """
    stack = []
    # Словарь для хранения соответствий скобок
    brackets = {')': '(', '}': '{', ']': '['}

    for char in text:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if not stack:
                print(f"Обнаружена закрывающая скобка '{char}', для которой нет открывающей.")
                return False
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                print(f"Обнаружена закрывающая скобка '{char}', не соответствующая открывающей '{stack[-1]}'.")
                return False

    if not stack:
        return True
    else:
        print(f"Остались непарные открывающие скобки: {stack}")
        return False
    
if __name__ == "__main__":
    texts = [
        "{[()()]()}",
        "{[(])}",
        "{{[[(())]]}}",
        "({[()])}",
        "({[(])}",
        "()[]{}",
        "([{}])",
        "(((",
        ")))",
        "([)]"
    ]

    for text in texts:
        result = check_brackets(text)
        print(f"Текст: {text}\nСоответствие скобок: {result}\n")