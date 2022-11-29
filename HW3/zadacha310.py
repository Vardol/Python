# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.

# поскольку принцип перевода из 10ной системы примерно тот же для всех систем исчисления - я сделал универсальную функцию,
# в нее можно передать значение целевой системы счисления. По умолчанию она переводит в 16-ричную.
# будем для простоты считать, что в задаче имеется в виду целое десятичное число

def read_whole_number(promting_message = "введите целое число", err_message = "Введено не подходящее число/строка"):
    result = input(promting_message)
    negative_input = False
    if result[0] == "-":
        negative_input = True
        result = result[1:]
    if not result.isdigit():
        print(err_message)
        result = read_whole_number(promting_message, err_message)
        return int(result)
    else:
        if negative_input: return -int(result)
        else: return int(result)


def convert_numeric_system_from_dec(decimal: int, numeric_system = 16):
    chars_tuple = ("0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    negative_input = False
    result = ""
    if decimal < 0:
        negative_input = True
        decimal=abs(decimal)

    if numeric_system <= 1 or numeric_system > len(chars_tuple): return "numeric system out of bounds"

    if decimal < numeric_system:
        result = chars_tuple[decimal] + result
        if negative_input: result = "-"+result
        return result
    else:
        result = chars_tuple[(decimal % numeric_system)] + result
        result = convert_numeric_system_from_dec(decimal // numeric_system, numeric_system) + result
        if negative_input: result = "-"+result
        return result
    

print(convert_numeric_system_from_dec(read_whole_number("введите целое число, которое надо перевести в 16-ричную систему - "), 16))