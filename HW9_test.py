 # HW9. Послідовність цілих чисел.
 # Программа запрашивает ввод, с клавиатуры, целых чисел, пока не будет введён 0. Как только пользователь
 # введёт 0 (ноль), программа должна вывести на экран следующие результаты (без учёта последнего 0):
 # количество введённых чисел, их сумму
 # среднее арифметическое всех введённых чисел
 # максимальное и минимальное значение
 # количество чётных и не чётных значений
 # Применение списков недопустимо!

Number_cnt = 0
Number_sum = 0
Min_number = 0
Max_number = 0
Chet_cnt_number = 0
NeChet_cnt_numbers = 0

while True:
    N = int(input('Введіть ціле число, або число "0", якщо треба припинити: '))
    if N == 0:
        break
    Number_sum += N
    Number_cnt += 1
    if Max_number == 0 or N > Max_number:
        Max_number = N
    if Min_number == 0 or N < Min_number:
        Min_number = N
    if N % 2:
        NeChet_cnt_numbers += 1
    else:
        Chet_cnt_number += 1

print('Кількість чисел, не враховуючи "0": ', Number_cnt)
print('Сума чисел, не враховуючи "О": ', Number_sum)
print('Середнє арифметичне, округлене до сотих, не враховуючи "О": ', round(Number_sum / Number_cnt, 2))
print('Максимальне значення, не враховуючи "О": ', Max_number)
print('Мінімальне значення, не враховуючи "0": ', Min_number)
print('Кількість парних значень, не враховуючи "0": ', Chet_cnt_number)
print('Кількість непарних значень, не враховуючи "О": ', NeChet_cnt_numbers)
