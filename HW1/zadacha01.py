# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.


day_of_week = float(input('Введите день недели цифрой - '))

if day_of_week != int(day_of_week):
    day_of_week = -1

#day_of_week = int(day_of_week)
if day_of_week <= 0 or day_of_week >= 8:
    print("нет такого дня недели")
elif day_of_week == 6 or day_of_week == 7:
    print("УРА!!! Выходной!")
else:
    print("Не выходной (((")