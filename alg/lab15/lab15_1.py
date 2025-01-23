def Equal(p, q):
    """
    Проверяет, равны ли два многочлена p и q.

    Параметры:
    p (list): Список коэффициентов многочлена p, начиная с коэффициента при x^0.
    q (list): Список коэффициентов многочлена q, начиная с коэффициента при x^0.

    Возвращает:
    bool: True, если многочлены равны, иначе False.
    """
    # Удаляем ведущие нули
    def trim(z):
        while len(z) > 1 and z[-1] == 0:
            z.pop()
        return z

    p_clean = trim(p.copy())
    q_clean = trim(q.copy())

    return p_clean == q_clean

def Summa(p, q):
    """
    Складывает два многочлена p и q.

    Параметры:
    p (list): Список коэффициентов многочлена p, начиная с коэффициента при x^0.
    q (list): Список коэффициентов многочлена q, начиная с коэффициента при x^0.

    Возвращает:
    list: Список коэффициентов многочлена r = p + q.
    """
    # Определяем максимальную длину списков
    max_len = max(len(p), len(q))
    # Создаем список для результата с нулевыми коэффициентами
    r = [0] * max_len

    # Складываем коэффициенты
    for i in range(max_len):
        coeff_p = p[i] if i < len(p) else 0
        coeff_q = q[i] if i < len(q) else 0
        r[i] = coeff_p + coeff_q

    # Удаляем ведущие нули
    while len(r) > 1 and r[-1] == 0:
        r.pop()

    return r

if __name__ == "__main__":
    p = [3, 2, 5]  # 3 + 2x + 5x^2
    q = [1, 4, 5]  # 1 + 4x + 5x^2
    r = [4, 6, 10]  # 4 + 6x + 10x^2

    print("Многочлен p:", p)
    print("Многочлен q:", q)
    print("Многочлен r = p + q:", Summa(p, q))
    print("Равны ли p и q?", Equal(p, q))
    print("Равны ли p и r?", Equal(p, r))