# 1) Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в середине,
# а вначале и в конце пробелы могут быть). Пока он не введёт правильно, просите его ввести. Функция
# # возвращает введённое слово
#


def enter_text(inp_text):
    while ' ' in inp_text.strip():
        inp_text = input('Enter your text here:')
    return inp_text


print(enter_text(input("Enter your text here:")))

# 2)	Пишем функцию, которая попросит ввести число. Пока он не введёт правильно, просите его ввести. Функция
# возвращает введённое число.


def enter_number(text):
    while not text.isdigit():
        text = input("Text not a number, pls enter correct:")
    return text


print(enter_number(input("Enter you number:")))