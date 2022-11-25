# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

# будем считать, что если цифры равны, то это тоже "да"

def string_isfloat(input_string: str):
    for i in range(0,len(input_string)):
        if not input_string[i].isdecimal() and input_string[i] != "." and input_string[i] != "-":
            return False
    return True


def read_float(promting_message = "введите число - ", err_message = "Введено не число."):
    result = input(promting_message)
    if not string_isfloat(result):
        print(err_message)
        result = read_float(promting_message, err_message)
        return result
    else:
        return result


number = read_float()

result = True
for i in range(0,len(number)-1):
    if number[i].isdigit():
        if number[i+1].isdigit():
            if number[i] > number[i+1]:
                result = False
                break
        elif number[i+2].isdigit() and number[i] > number[i+2]:
            result = False
            break

print(result)

    
