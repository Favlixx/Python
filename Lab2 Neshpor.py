# Лаб работа №2
# Нешпор Семен, 100502-УБТа-о23, Вариант 19 (4)

import math as m
import sys

x = float(input('Введите значение х: '))
y = float(input('Введите значение y: '))

f = float(input('Выберите функцию (номер): \n1) arcsin(y/x) \n2) e^y \n3) ln(x*y) \n'))
d = None

match f:
    case 1:
        if abs(y / x) > 1:
            x = float(input('Выберите другое значение x: '))
            y = float(input('Выберите другое значение y: '))
        f = m.asin(y/x)
    case 2:
        f = m.exp(y)
    case 3:
        f = m.log(x*y)
    case _:
        print('Некорректный выбор функции')
        sys.exit()

if x > y:
    d = (f - y)**(1/3) + m.tan(f)

if x < y:
    d = (y - f)**3 + m.cos(f)

if x == y:
    d = (y + f)**2 + x**3

print('Результат: ', d)