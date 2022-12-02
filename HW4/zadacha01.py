# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def list_summ(mylist: list):
    result = 0
    for i in range(1, len(mylist), 2):
        result += mylist[i]
    return result

def fill_array_random(input_array: list, min = -10, max = 10):
    import random
    for i in range(0,len(input_array)):
        input_array[i] = random.randint(min,max)
    return input_array

numbers_list = [0] * 5
numbers_list = fill_array_random(numbers_list)

print(numbers_list)
print(list_summ(numbers_list))