# HW19. Функція is_year_leap

"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
если год високосный, и False иначе.
"""
# Вариант 1

year = int(input("Введіть рік, щоб з'ясувати високосний він чи ні: "))


def is_year_leap(year):
    if year == 2100 or year == 2200 or year == 2300:
        return "False, рік не високосний", year
    elif year % 100 == 0 and year % 400 != 0:
        return "False, рік не високосний", year
    elif year % 4 == 0 or year % 400 == 0:
        return "True, рік високосний", year
    else:
        return "False, рік не високосний", year


print(is_year_leap(year))

# Вариант 2

year = int(input("Введіть рік, щоб з'ясувати високосний він чи ні: "))


def is_year_leap(year):
    if year == 2100 or year == 2200 or year == 2300:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 or year % 400 == 0:
        return True
    else:
        return False

print(is_year_leap(year))