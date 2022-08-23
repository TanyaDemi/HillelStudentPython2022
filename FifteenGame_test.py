from random import randint


class FifteenGame:
    def __init__(self):
        self.elements = {}
        self.position = None

    # Будова поля гри
    def table_field(self):
        d = self.elements
        print('+----+----+----+----+')
        print('|{:^4}|{:^4}|{:^4}|{:^4}|'.format(d[1], d[2], d[3], d[4]))
        print('+----+----+----+----+')
        print('|{:^4}|{:^4}|{:^4}|{:^4}|'.format(d[5], d[6], d[7], d[8]))
        print('+----+----+----+----+')
        print('|{:^4}|{:^4}|{:^4}|{:^4}|'.format(d[9], d[10], d[11], d[12]))
        print('+----+----+----+----+')
        print('|{:^4}|{:^4}|{:^4}|{:^4}|'.format(d[13], d[14], d[15], d[16]))
        print('+----+----+----+----+')

    # Форматування запису числа у клітинці
    def format_tablet(self, tablet):
        tablet = tablet.strip()
        if len(tablet) == 1:
            return '  ' + tablet + ' '
        elif len(tablet) == 2:
            return ' ' + tablet + ' '
        elif len(tablet) == 0:
            return '    '

    # Рандомне заповнення гри.
    def build_field(self, begining):
        for y in range(1, 17):
            self.elements[y] = self.format_tablet(str(y))
        for a, b in self.elements.items():
            if b == ' 16 ':
                self.elements[a] = '    '
                break
        self.position = a
        for _ in range(100):
            lst = self.valid_moves()
            lst1 = []
            for x in lst:
                lst1.append(int(x.strip()))
            self.change(lst1[randint(0, len(lst1) - 1)])

    # Рух клітинок у грі
    def change(self, new):
        real = self.position
        for a, b in self.elements.items():
            if b == self.format_tablet(str(new)):
                new = a
                break
        self.elements[real], self.elements[new] = self.elements[new], self.elements[real]
        self.position = new

    # Запропоновані варіанти можливого переміщення у грі
    def valid_moves(self):
        pos = self.position
        if pos == 1:
            return self.elements[pos + 1], self.elements[pos + 4]
        elif pos == 4:
            return self.elements[pos - 1], self.elements[pos + 4]
        elif pos == 13:
            return self.elements[pos + 1], self.elements[pos - 4]
        elif pos == 16:
            return self.elements[pos - 1], self.elements[pos - 4]
        elif pos in [5, 9]:
            return self.elements[pos + 1], self.elements[pos - 4], self.elements[pos + 4]
        elif pos in [8, 12]:
            return self.elements[pos - 1], self.elements[pos - 4], self.elements[pos + 4]
        elif pos in [2, 3]:
            return self.elements[pos - 1], self.elements[pos + 1], self.elements[pos + 4]
        elif pos in [14, 15]:
            return self.elements[pos - 1], self.elements[pos + 1], self.elements[pos - 4]
        elif pos in [6, 7, 10, 11]:
            return self.elements[pos - 1], self.elements[pos + 1], self.elements[pos - 4], self.elements[pos + 4]

    # Закінчення гри
    def game_over(self):
        flag = False
        for a, b in self.elements.items():
            if b == '    ':
                pass
            else:
                if a == int(b.strip()):
                    flag = True
                else:
                    flag = False
        return flag


g = FifteenGame()
g.build_field(int(input('Натисніть будь-яку цифру для початку гри: ')))
print('Натисніть "0" для закінчення гри: ')
g.table_field()
while True:

    print('Натисніть номер елементу "№" який бажаєте пересунути на вільне місце, з наведених нижче.')
    lst = g.valid_moves()
    lst1 = []
    for y in lst:
        lst1.append(int(y.strip()))
        print(y.strip(), '\t', end='')
    print()
    element = int(input())
    if element == 0:
        break
    elif element not in lst1:
        print('Хід не можливий')
    else:
        g.change(element)
    g.table_field()
    if g.game_over():
        break
        print('Перемога!')
