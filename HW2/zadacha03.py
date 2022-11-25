# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

# с учетом того, что это зарплата - оно д.б. не просто целым, но еще и натуральным.

def read_natural_int(promting_message = "введите натуральное число", err_message = "Введено не подходящее число/строка"):
    result = input(promting_message)
    if not result.isdigit() or int(result) == 0: #Сначала проверяем на "циферность", т.к. если там буквы, то преобразование в число для сравнения с нулем выдаст ошибку
        print(err_message)
        result = read_natural_int(promting_message, err_message)
        return int(result)
    else:
        return int(result)


banknotes_count = 0
salary = read_natural_int("Введите зарплату без копеек - ", "Не может быть такой зарплаты или ввели с копейками...")

for i in 25,10,3,1:
    print(str(i) + " рублевых купюр - " + str(salary // i))
    banknotes_count += salary // i
    salary %= i
print(f"Всего - {banknotes_count} купюр")