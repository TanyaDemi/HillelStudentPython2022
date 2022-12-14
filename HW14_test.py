# HW14. Сусіди.
# Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей
# (слева и справа), и выведите количество таких элементов. Крайние элементы списка никогда не учитываются,
# поскольку у них недостаточно соседей.

from random import randint

lst = []
for _ in range(20):
    lst.append(randint(10, 99))
print(lst)

cnt = 0
for i in range(1, len(lst)-1):
    if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
        cnt += 1
print(cnt)
