# HW21. Функция square
"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения:
периметр квадрата, площадь квадрата и диагональ квадрата.
"""

Side = int(input("Введіть значення сторони квадрата, см: "))


def square():
    S = Side * Side
    P = Side * 4
    D = round(Side * 2 ** 0.5, 2)
    return "Площа квадрата, кв.см", S, "Периметр квадрата, см", P, "Діагональ квадрата, см", D


print(square())
