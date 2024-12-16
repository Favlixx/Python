# Лаб. работа №3
# Нешпор Семен, 100502-УБТа-о23, Вариант 19 (4)

# С помощью цикла for
import math as m

x1 = 2
xn = 5
dx = 0.1
a = 4
b = 7
per = int((xn - x1) / dx)

results = []

for x in range(per):
    x = x1 + x * dx
    y = b * x * m.sqrt(1 + a**2 * m.log(x))
    results.append((x, y))

for x, y in results:
    print(f"x = {x:.2f}, y = {y:.4f}")


# С помощью цикла While
import math as m

x1 = 2
xn = 5
dx = 0.1
a = 4
b = 7

results = []

x = x1
while x <= xn:
    y = b * x * m.sqrt(1 + a**2 * m.log(x))
    results.append((x, y))
    x += dx

for x, y in results:
    print(f"x = {x:.1f}, y = {y:.4f}")