# 2-Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math

def mult_list(input_list: list):
    result = []
    for i in range(0, math.ceil(len(input_list) / 2)):
        result.append(input_list[i] * input_list[len(input_list) - 1 - i])
    return result

print(mult_list([2, 3, 4, 5, 6]))
