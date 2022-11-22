# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input("введите номер четверти - "))

if quarter_number not in range(1, 5) : print("введен некорректный номер четверти")
elif quarter_number == 1 : print("x > 0, y > 0")
elif quarter_number == 2 : print("x < 0, y > 0")
elif quarter_number == 3 : print("x < 0, y < 0")
elif quarter_number == 4 : print("x > 0, y < 0")