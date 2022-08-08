# HW28. Ромб 2

"""
При помощи вложенных циклов (можно while, можно for) и оператора IF нарисовать фигуры представленные ниже.
Пользователь вводит, с клавиатуры, высоту фигуры в символах.

  D         *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *         *         *
    *       *       *
      *     *     *
        *   *   *
          * * *
            *

"""

height = int(input('Прошу ввести непарне значення, яке буде позначати висоту фігури у символах: '))

for y in range(height):
    for x in range(height):
        if (
            y <= height // 2 and height // 2 - y <= x <= height // 2 + y
            or x == height // 2
            or y > height // 2 and y - x == height // 2
            or y > height // 2 and x == height - 1 + (height // 2 - y)
        ):
                print(' *', end='')
        else:
            print('  ', end='')
    print()
