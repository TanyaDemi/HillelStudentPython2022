# HW30 Цифровий лічильник.

# Реализовать класс цифрового счетчика. В классе реализовать методы: установки максимального, минимального
# и начального значения счётчика (предусмотреть установку счётчика значениями по умолчанию 0-100) увеличения
# счетчика на 1 возвращения текущего значения счётчика.
# Можно добавить дополнительные методы, на ваше усмотрение, но только после обязательной части ДЗ.

class DigitalCounter:
    start = 0
    end = 100
    current = None


    def __init__(self, start=0, end=100, current=None):
        self.start_value = start
        self.current_position = current
        self.stop_counter = end

    def display_info(self):
        print('-' * 30)
        print('Лічильник №307584572, 2022р.')
        print('-' * 30)
        print(f'Start: \t {self.start_value}')
        print('-' * 30)
        print(f'Current: \t {self.current_position}')
        print('-' * 30)
        print(f'Stop: \t {self.stop_counter}')
        print('-' * 30)
        print(f'Показання лічильника: {c.increase()}')
        print('-' * 30)


    def increase(self, step=1):
        if self.current_position + step < self.stop_counter:
            self.current_position += step
            return self.current_position
        else:
            return print('Заміна лічильника!')

    def get_current_value(self):
        if self.start_value < self.current_position < self.stop_counter:
            return self.current_position
        else:
            return print('Лічильник зламаний!')


c = DigitalCounter(1, 99, 52)
c.display_info()
print(f'Показання лічильника: {c.increase()}')
