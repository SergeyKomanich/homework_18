"""
При помощи вложенных циклов (можно while, можно for) и оператора IF нарисовать ромб.
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
"""
height_diamond = int(input('Введите число(высота ромба): '))
for i in range(2 * height_diamond + 1):
    if i <= height_diamond:
        print('  ' * (height_diamond - i) + ' *' * (i + 1) + ' *' * i)  # СОЗДАЕМ ПЕРВУЮ ПИРАМИДУ
    else:
        if i == (height_diamond * 2):    # СОЗДАЕМ ПЕРЕВЕРНУТУЮ ПИРАМИДУ
            print('  ' * height_diamond + ' *')
        else:
            print('  ' * (i - height_diamond) + ' *', end='')
            print('  ' * (4 * height_diamond - 2 * i - 1) + ' *')