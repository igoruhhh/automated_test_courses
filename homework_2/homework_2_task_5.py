# coding=utf-8
# Дано три числа. Упорядочите их в порядке возрастания. Программа должна считывать три числа a, b, c, затем
# программа должна менять их значения так, чтобы стали выполнены условия a <= b <= c, затем программа выводит
# тройку a, b, c./
a = 90
b = 100
c = 80
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
    print(a, b, c)


