# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

def convert_decimal_to_binary(decimal: int):
    result = ""
    if decimal == 1:
        result = "1" + result
        return result
    else:
        result = str(decimal % 2) + result
        result = convert_decimal_to_binary(decimal // 2) + result
        return result

print(convert_decimal_to_binary())