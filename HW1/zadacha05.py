# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#AB = √(xb - xa)2 + (yb - ya)2

xa = float(input("введите координату х первой точки - "))
ya = float(input("введите координату y первой точки - "))

xb = float(input("введите координату х второй точки - "))
yb = float(input("введите координату y второй точки - "))

print("Расстояние между точками = ", (((xb - xa)**2 + (yb - ya)**2)**0.5))