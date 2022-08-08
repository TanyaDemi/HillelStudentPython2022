# HW27. Ромб 1

"""
При помощи вложенных циклов (можно while, можно for) и оператора IF нарисовать фигуры представленные ниже.
Пользователь вводит, с клавиатуры, высоту фигуры в символах.
  C         *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *                   * 
    *               *
      *           *
        *       *
          *   *
            *

height = int(input('Высота пирамиды: '))
for j in range(1, height + 1):
  for i in range(height * 2 + 1):
    if i == height:
      print('#' * (j * 2 - 1), end = "")
      height -= 1
    else:
      print(' ', end = "")
  print()
"""
height = int(input('Прошу ввести непарне значення, яке буде позначати висоту фігури у символах: '))

for y in range(height):
    for x in range(height):
        if (
            y <= height // 2 and height // 2 - y <= x <= height // 2 + y
            or y > height // 2 and y - x == height // 2
            or y > height // 2 and x == height - 1 + (height // 2 - y)
        ):
                print(' *', end='')
        else:
            print('  ', end='')
    print()
