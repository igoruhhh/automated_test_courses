# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
# Учитываем, что может быть повторяющиеся значения аргументов..


def premin(*numbers):
    l = list(numbers)
    l.sort()
    min_element = l[0]
    for element in l:
        if element > min_element:
            return element


print(premin(2, 2, 3, 4, 5))
