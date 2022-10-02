# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def read_natural():
    result = input("Введите натуральное число N - ")
    if not result.isdigit():
        print("Введено не подходящее число/строка")
        result = read_natural()
        return result
    else:
        return result

def check_if_number_is_palindrom(x: str):
    if len(x) == 1:
        return True
    for i in range(0,len(x)//2):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True

def revert_number_in_string(x: str):
    if len(x) == 1:
        return x
    result = ""
    for i in range(0,len(x)):
        result += (x[len(x) - 1 - i])
    return result

def summ_with_reverted(x: str):
    return str(int(x) + int(revert_number_in_string(x)))

def number_palindrom(x: str):
    if check_if_number_is_palindrom(x):
        return x
    else:
        return number_palindrom(summ_with_reverted(x))


print("палиндром введенного числа - " + number_palindrom(read_natural()))