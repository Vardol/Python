# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)


def read_natural_int(promting_message = "введите натуральное число - ", err_message = "Введено не подходящее число/строка - "):
    result = input(promting_message)
    if not result.isdigit() or int(result) == 0: #Сначала проверяем на "циферность", т.к. если там буквы, то преобразование в число для сравнения с нулем выдаст ошибку
        print(err_message)
        result = read_natural_int(promting_message, err_message)
        return int(result)
    else:
        return int(result)

def create_2d_array(xsize, ysize):
    result = [0] * xsize
    for i in range(0, xsize):
        result[i] = [0] * ysize
    return result
        
def fill_2d_array_random(input_array: list, min = -10000, max = 10000):
    import random
    for i in range(0,len(input_array)):
        for j in range(0,len(input_array[i])):
            input_array[i][j] = random.randint(min,max)
    return input_array

def print_array(input_array: list):
    if str(type(input_array[0])) == "<class 'list'>":
        for i in range(0,len(input_array)):
            print_array(input_array[i])
    else:
        print(input_array)

def average(input_list: list):
    result = 0
    for i in (input_list):
        result += i
    result /= len(input_list)
    return result

my_2d_array = fill_2d_array_random(create_2d_array(read_natural_int(),read_natural_int()), -10, 10)

for i in range(0,len(my_2d_array)):
    print(my_2d_array[i], end = "")
    print(" Average = ", end = "")
    print(average(my_2d_array[i]))

