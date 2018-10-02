# Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами и если существует, то
# возвращает тип треугольника Equilateral triangle (равносторонний),
# Isosceles triangle (равнобедренный),
# Versatile triangle (разносторонний)
# или не треугольник (Not a triangle).


def task_7(a, b, c):
    if ((a + b) <= c) or ((b + c) <= a) or ((a + c) <= b):
        print("Not a triangle")
    elif a == b == c:
        print("Equilateral triangle")
    elif a == b or a == c or b == c:
        print("Isosceles triangle")
    else:
        print("Versatile triangle")


task_7(5, 4, 3)
