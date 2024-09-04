# Лаб 1. Задание 3. Вариант 8

# Дан массив из п четырехзначных натуральных чисел. Выведите
# на экран только те, у которых сумма первых двух цифр равна сумме
# двух последних.

import random

def check_numbers(numbers):
    for num in numbers:
        str_num = str(num)
        
        if len(str_num) != 4:
            continue
        
        sum1 = int(str_num[0]) + int(str_num[1])
        
        sum2 = int(str_num[2]) + int(str_num[3])
        
        if sum1 == sum2:
            print(num)

numbers = [round(random.randrange(0, 9999), 2) for _ in range(25)]
print(numbers)
check_numbers(numbers)