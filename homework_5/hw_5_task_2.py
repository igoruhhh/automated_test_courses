"""
Задание 2 (на создание классов)
Создать классы
1) Прямоугольная площадка (пример: комната) (свойства: две стороны).
Методы:
1.	вычисляем площадь,
2.	вычисляем периметр.
2) Точка на карте (свойства: X, Y).
Методы:
1.	Нужно вычислить расстояние до начала координат,
2.	* вычисляется расстояние между точкой и другой точкой экземпляром этого же класса
3.	** перевод в другие системы координат
"""
import math


class rectangular_area():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        square = self.a * self.b
        return square

    def perimeter(self):
        perim = (self.a + self.b) * 2
        return perim


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_start(self):
        distance = ((self.x - 0) ** 2 + (self.y - 0) ** 2) ** 0.5
        return distance

    def translate_into_polar(self):
        l = self.distance_to_start()
        alpha = math.atan2(self.y, self.x)
        return l, math.degrees(alpha)


def distance_between_points(point1, point2):
    distance = ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5
    return distance


if __name__ == "__main__":
    room1 = rectangular_area(4,4)
    print("Square is", room1.square())
    print("Perimeter is", room1.perimeter())
    point1 = point(0, 3)
    point2 = point(4, 0)
    print(point1.distance_to_start())
    print(point2.distance_to_start())
    print("New coordinates", point1.translate_into_polar())
    print("New coordinates", point2.translate_into_polar())
    print(distance_between_points(point1, point2))
