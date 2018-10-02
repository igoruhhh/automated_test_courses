
# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.


def distance(x1, y1, x2, y2):
    dis = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    return dis


x1 = float(input('Enter X1'))
y1 = float(input('Enter Y1'))
x2 = float(input('Enter X2'))
y2 = float(input('Enter Y2'))

print(distance(x1, y1, x2, y2))
