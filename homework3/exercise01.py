# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# считаем, что позиция = индекс.

def list_summ(mylist: list):
    result = 0
    for i in range(1, len(mylist), 2):
        result += mylist[i]
    return result

numbers_list = [2, 3, 5, 9, 3]

print(list_summ(numbers_list))