 # HW8. Знайти найбільший цілий ступінь двійки. Программа запрашивает ввод,
 # с клавиатуры, целых чисел, пока не будет введён 0. Как только пользователь введёт 0 (ноль),
 # программа должна вывести на экран следующие результаты (без учёта последнего 0):
 # количество введённых чисел их сумму
 # среднее арифметическое всех введённых чисел
 # максимальное и минимальное значение
 # количество чётных и не чётных значений
 # Применение списков недопустимо!

N = int(input('Вкажіть ціле натуральне число N:  ', ))
Number = 2
Degree_Number = 1

while Number <= N:
    Number *= 2
    Degree_Number += 1

print(Degree_Number - 1, Number // 2, end='           ')
print("2 **", Degree_Number - 1, "= ", Number // 2, end='         ')