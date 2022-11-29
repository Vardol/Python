# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

# в задаче это не уточнено, поэтому будем считать, что речь о стандартной записи дробного числа в виде +(-)X...Y.Z...W

def string_isfloat(input_string: str):
    if input_string[0] == "-" or input_string[0] == "+": input_string = input_string[1:]
    # если в начале строки стоит - или +, то это допустимо, но мы их убираем для простоты дальнейшей обработки

    dot_index = input_string.find(".")

    if dot_index <= 0 or dot_index >= len(input_string) - 1: return False
    #если точка стоит в первой или последней позиции, то это тоже не число, т.к. число не может начинаться или заканчиваться точкой.

    if int(input_string[dot_index+1:]) == 0 : return False
    # если дробная часть написана, но равна 0, то считаем, что это не дробное число.

    for i in range(0,dot_index):
        if not input_string[i].isdecimal():
            return False
    # будем считать, что в задаче речь о десятичном числе

    for i in range(dot_index + 1, len(input_string)):
        if not input_string[i].isdecimal():
            return False

    return True


print(string_isfloat(input("введите дробное число - ")))