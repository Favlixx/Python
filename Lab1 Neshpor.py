# Лаб работа №1
# Нешпор Семен, 100502-УБТа-о23, Вариант 19 (4)

import math as m
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
z = float(input("Введите значение z -> "))

a = abs(m.cos(x) - m.cos(y))
b = 2 * (m.sin(y))**2
c = 1 + z + ((z**2) / 2)

s = (a**b) * c

print('Результат: ', s)