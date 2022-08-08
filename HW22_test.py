# HW22 Бухгалтерська книга
"""
 Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся
записи о номере заказа, названии книги, количестве и стоимости одной книги, как
представлено ниже, в таблице.
+--------------+------------------------------------+----------+----------------+
| Order Number |       Book Title and Author        | Quantity | Price per Item |
+--------------+------------------------------------+----------+----------------+
|        34587 | Learning Python, Mark Lutz         |        4 |          40.95 |
|        98762 | Programming Python, Mark Lutz      |        5 |          56.80 |
|        77226 | Head First Python, Paul Barry      |        3 |          32.95 |
|        88112 | Einfuhrung in Python3, Bernd Klein |        3 |          24.99 |
+--------------+------------------------------------+----------+----------------+
Напишите программу на Python, которая на вход получает список списков:
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения
цены на товары и количества. Стоимость заказа должна быть увеличена на $10, если она
меньше $100. Программа должна использовать lambda, map, однострочный if, round и list.
Решение задачи должно быть выполнено в ОДНУ СТРОКУ!
"""

listABook = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

quantity_x_price = list(map(lambda i: (i[0], round((i[2] * i[3]), 2) + 10 if round((i[2] * i[3]), 2) <= 100 else round((i[2] * i[3]), 2)), listABook))

print('№ заказа:', listABook[0][0], 'Загальна вартість:', quantity_x_price[0][1])
print('№ заказа:', listABook[1][0], 'Загальна вартість:', quantity_x_price[1][1])
print('№ заказа:', listABook[2][0], 'Загальна вартість:', quantity_x_price[2][1])
print('№ заказа:', listABook[3][0], 'Загальна вартість:', quantity_x_price[3][1])

print(quantity_x_price)
