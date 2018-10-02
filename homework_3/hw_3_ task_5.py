# Задание 5
# Создайте строку, в которой написан, какой-то текст. Пример:
# We are not what we should be!
# We are not what we need to be.
# But at least we are not what we used to be
#  (Football Coach)
# •	Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
# •	Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
# •	Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)

text = ("We are not what we should be!")
l = len(text.split(" "))
listWords = []
for i in text.split(" "):
    listWords.append(i)
for g in range(len(listWords)):
    listWords[g] = listWords[g].strip("!")
    listWords[g] = listWords[g].strip(".")
print(listWords)
