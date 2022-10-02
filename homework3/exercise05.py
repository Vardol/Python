# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(number: int):
    result = [0]
    if number >= 1:
        result.append(1)
    if number >= 2:
        for i in range(2, number + 1):
            result.append(result[i - 1] + result[i - 2])
    return result

def negative_fibonacci(number: int):
    result = []
    if number <= -1:
        result.insert(0, 1)
    if number <= -2:
        result.insert(0, -1)
    if number <= -3:
        for i in range(3, -number + 1):
            result.insert(0, result[1] - result[0])
    return result

def universal_fibonacci(number: int):
    result = negative_fibonacci(-number)
    result += fibonacci(number)
    return result

print(universal_fibonacci(10))