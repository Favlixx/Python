# Лаб работа №5
# Нешпор Семен, 100502-УБТа-о23, Вариант 19 (4)

# Задание 1
numbers = input('Введите целые числа через пробел: ', ).split()
numbers = [int(num) for num in numbers]

max_num = max(numbers)
index_max = numbers.index(max_num)

print('Максимальный элемент в списке: ', max_num, '\nИндекс максимального элемента: ', index_max)

# Задание 2
numbers = input('Введите целые числа через пробел: ', ).split()
numbers = [int(num) for num in numbers]

numbers1 = []

for i in numbers:
    if i % 2 != 0:
        numbers1.append(i)

numbers1.sort(reverse=True)

if numbers1:
    print('Результат: ', numbers1)
else:
    print('Таких чисел нет')