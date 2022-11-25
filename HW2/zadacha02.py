# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

# с учетом того, что Х - количество вводимых чисел, оно д.б. не просто целым, но еще и натуральным.

def read_natural_int(promting_message:str):
    result = input(promting_message)
    if not result.isdigit() or int(result) == 0: #Сначала проверяем на "циферность", т.к. если там буквы, то преобразование в число для сравнения с нулем выдаст ошибку
        print("Введено не подходящее число/строка")
        result = read_natural_int(promting_message)
        return int(result)
    else:
        return int(result)

count = 0
while count <=1:
    count = read_natural_int("Из скольки чисел будем искать два максимума - ")
    if count == 1:
        print("Не получится выбрать 2 максимальных числа из одного...")

max1 = int(input("Введите первое число - "))
max2 = int(input("Введите следующее число - "))

if max1 < max2:
    swap_value = max1
    max1 = max2
    max2 = swap_value
count -= 2

while count > 0:
    new_number = int(input("Введите следующее число - "))
    if new_number > max1:
        max2 = max1
        max1 = new_number
    elif new_number > max2:
        max2 = new_number
    count-=1

print("Максимальное чило - " + str(max1) + ". Второе максимальное число - " + str(max2) + ".")