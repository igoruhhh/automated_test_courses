# 1). Написать функцию is_year_leap, принимающую 1 аргумент — год, и
# возвращающую True, если год високосный, и False иначе.
year = int(input())


def is_year_leap(year):
    if (year % 4 == 0 and not year % 100 == 0) or year == 0 or year % 400 == 0:
        return True
    else:
        return False


print(is_year_leap(year))


# 2)
# #Функция принимает три числа a, b, c. Функция должна определить,
# существует ли треугольник с такими сторонами. Если треугольник
# существует, вернёт True, иначе False.

def func(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


a = int(input())
b = int(input())
c = int(input())

print(func(a, b, c))
