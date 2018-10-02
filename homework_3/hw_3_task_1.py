# # Задание 1
# Входные данные
# Пользователь вводит строку. Выловите исключения, если введённая строка слишком
# короткая.
s = input("Enter a string: ")
if len(s) < 5:
    raise NameError('String is too small')
print(s[2], s[len(s)-2], s[0:5], s[0:len(s)-2], s[1::2], s[2::2], s[::-1], s[::-2], len(s), sep='\n')