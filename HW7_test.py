# HW7
# Квадрати натуральних чисел. По данному целому числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N, в порядке возрастания. Примеры:
# 50      1 4 9 16 25 36 49
# 10      1 4 9
# 9       1 4 9
# 4       1 4
# 1       1
# 100     1 4 9 16 25 36 49 64 81 100
# 99      1 4 9 16 25 36 49 64 81
# Пользователь вводит число, например 50, программы должна в ответ вывести:
# 50      1 4 9 16 25 36 49

N = int(input('Вкажіть ціле число N: ', ))
print('Ряд квадратів натуральних чисел за зростанням не більше N:')
cnt = 1
while cnt ** 2 <= N:
    print(cnt ** 2, end=' ')
    cnt += 1



