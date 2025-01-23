import random

def kth_statistic(numbers, k):
    if not numbers:
        raise ValueError("Список пуст.")
    if 1 <= k <= len(numbers):
        pivot = random.choice(numbers)
        lows = [el for el in numbers if el < pivot]
        highs = [el for el in numbers if el > pivot]
        pivots = [el for el in numbers if el == pivot]
        if k <= len(lows):
            return kth_statistic(lows, k)
        elif k > len(lows) + len(pivots):
            return kth_statistic(highs, k - len(lows) - len(pivots))
        else:
            return pivots[0]
    else:
        raise ValueError("Значение k выходит за пределы допустимого диапазона.")

def main():
    numbers = [7, 10, 4, 3, 20, 15]
    k = 3
    try:
        result = kth_statistic(numbers, k)
        print(f"{k}-й статистикой является {result}.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()