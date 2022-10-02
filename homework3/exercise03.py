# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

def maximum_defference_btw_decimalpart(input_list: list):
    max = input_list[0] % 1
    min = input_list[0] % 1

    for i in range(0, len(input_list)):
        if input_list[i] % 1 > max:
            max = input_list[i] % 1
        if input_list[i] % 1 < min:
            min = input_list[i] % 1
    return round(max - min, 8)


print(maximum_defference_btw_decimalpart([4.07, 5.1, 8.2444, 6.98]))