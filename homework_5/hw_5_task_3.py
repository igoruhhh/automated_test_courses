"""
Задание 3 (на создание тестов c помощью unittest)
Создайте наборы тестов на написанные функции из прошлого домашнего задания:
•	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
если год високосный, и False иначе.
•	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
Если треугольник существует, вернёт True, иначе False.
•	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами
и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный),
Versatile triangle (разносторонний) или не треугольник (Not a triangle).
"""
import unittest
from automated_test_courses.homework_3.hw_3_task_6 import is_year_leap
from automated_test_courses.homework_3.hw_3_task_6 import func


class IsyearleapTest(unittest.TestCase):
    def test_leap_year(self):
        res = is_year_leap(2000)
        self.assertEqual(res, True)

    def test_not_leap_year(self):
        res = is_year_leap(2001)
        self.assertEqual(res, False)
        res = is_year_leap(600)
        self.assertEqual(res, False)


class FuncTest(unittest.TestCase):
    def test_func(self):
        res = func(2, 3, 4)
        self.assertEqual(res, True)

    def test_treangle_does_not_exist(self):
        res = func(3, 6, 1)
        self.assertEqual(res, False)


if __name__ == "__main__":
    unittest.main()
