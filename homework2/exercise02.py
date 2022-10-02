# Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.

def read_natural():
    result = input("Введите натуральное число N - ")
    if not result.isdigit():
        print("Введено не подходящее число/строка")
        result = read_natural()
        return result
    else:
        return result

def mult(x: int, mylist: list):
    if x == 1:
        mylist.append(1)
        return
    else:
        mult(x-1, mylist)
        mylist.append(x * mylist[-1])
        return

result = []
mult(int(read_natural()),result)
print(result)