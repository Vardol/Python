# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

def fill_array_random(input_array: list, min = -10000, max = 10000):
    import random
    for i in range(0,len(input_array)):
        input_array[i] = random.randint(min,max)
    return input_array

def find_min_index(input_array: list, start_pos = 0, end_pos = -1):
    
    if end_pos not in range(start_pos, len(input_array)):
        end_pos = len(input_array) - 1
    
    min_index = start_pos

    for i in range(start_pos, end_pos + 1):
        if input_array[i] < input_array[min_index]:
            min_index = i
    return min_index


def sort_by_select(input_array: list):
    for i in range(0, len(input_array) - 1):
        min_index = find_min_index(input_array, i)
        swap_value = input_array[i]
        input_array[i] = input_array[min_index]
        input_array[min_index] = swap_value
    return input_array


my_array = [0] * 30
my_array = fill_array_random(my_array,-100,100)
print("")
print("Исходный сгенерированный массив - ", end = "")
print(my_array)
print("")
print("Отсортированный массив - ", end = "")
print(sort_by_select(my_array))
print("")