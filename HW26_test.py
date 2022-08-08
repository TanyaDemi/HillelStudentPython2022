# HW26. Трикутник 2
"""
При помощи вложенных циклов (можно while, можно for) и оператора IF нарисовать фигуры представленные ниже.
Пользователь вводит, с клавиатуры, высоту фигуры в символах.

  B         *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
"""

height = int(input('Прошу ввести значення, яке буде позначати висоту фігури у символах: '))

for y in range(height):
    for x in range(height * 2):
        if (
                y + x < height
                or x - y > height
                or y == height and 0 < x <= height * 2
        ):
                print("  ", end='')
        else:
            print(end=' *')
    print()
