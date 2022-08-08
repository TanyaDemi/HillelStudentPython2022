# HW17. Задача словники 2
"""
Дана строка (большая строка, лучше взять на английском).
Выведите слово, которое в этой строке встречается чаще всего. Если таких слов несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.
"""
from pprint import pprint

s = """ I call you when I need you my heart's on fire You come to me come to me wild and wired Mmm you come to me give me everything I need Give me a lifetime of promises and a world of dreams Speak a language of love like you know what it means Mmm it can't be wrong Take my heart and make it strong baby You're simply the best better than all the rest Better than anyone anyone I've ever met I'm stuck on your heart I hang on every word you say Tear us apart baby I would rather be dead You're simply the best better than all the rest Better than anyone anyone I've ever met I'm stuck on your heart I hang on every word you say Tear us apart baby I would rather be dead You're simply the best better than all the rest Better than anyone anyone I've ever met I'm stuck on your heart I hang on every word you say Tear us apart baby I would rather be dead """
d = {}
lst = s.split()
for w in lst:
    d[w] = d.get(w, 0) + 1
print("Слова та їх кількість: ")
pprint(d)

Maximum = max(d.values())
lst = set()
for key in d:
    if d[key] == maximum:
        lst.add(key)
        s = sorted(lst)
print("Слово, яке найбільше зустрічається у тексті: ", s[-1])
