# HW11. Строки та срізи.
# Дана строка (вводится с клавиатуры).a. выведите третий символ этой строки.
# b. выведите предпоследний символ этой строки.
# c. выведите первые пять символов этой строки.
# d. выведите всю строку, кроме последних двух символов.
# e. выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы
# выводятся начиная с первого).
# f. выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# g. выведите все символы в обратном порядке.
# h. выведите все символы строки через один в обратном порядке, начиная с последнего.
# i. выведите длину данной строки.
# Задача ДОЛЖНА состоять из 10 строк кода. Применение операторов: IF, WHILE, FOR или каких либо функций
# (кроме функции len()) НЕ ДОПУСТИМО!
# Использовать нужно ТОЛЬКО индексы и срезы.

s = input('Введіть рядок: ')
print('1. Tретій символ цього рядка: ', s[2])
print('2. Передостанній символ цього рядка: ', s[len(s)-2])
print("3. Перші п'ять символів цього рядка: ", s[0:5])
print('4. Весь рядок, крім двох останніх символів: ', s[:-2])
print('5. Символи з парними індексами: ', s[0::2])
print('6. Символи з непарними індексами: ', s[1::2])
print('7. Символи у зворотному порядку: ', s[::-1])
print('8. Символи рядка через один у зворотному порядку, починаючи з останнього: ', s[-1::-2])
print('9. Довжина рядка: ', len(s))
