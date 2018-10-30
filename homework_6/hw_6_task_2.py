"""
Задание 2
Задание из класса «Записываем “Number: строка из файла” из одного файла в другой»:
1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом для записи в файл
(кто сделал с помощью методов – делают с помощью print, кто сделал с помощью print – делают с помощью методов)
2. Воспользуйтесь менеджером контекста для файла (with … as), в который вы записываете информацию.
Задание: 1) Создать текстовый файл и записать в него вашу песню “la-la-la”.
        2) Прочитать и вывести на экран код файла, в котором вы создавали класс Person
"""


def song_generation(rows=3, la=3, end_of_song=0):
    """
    Function will generate the best song you've ever heard
    """
    song = "la-" * la
    song = song.strip("-")
    if end_of_song:
        song = (song + "\n") * (rows - 1) + (song + "!" + "\n")
    else:
        song = (song + "\n") * (rows - 1) + (song + "." + "\n")
    #    print(song)
    return song


if __name__ == "__main__":

    # 1) Создать текстовый файл и записать в него вашу песню “la-la-la”.
    try:
        f = open("temp.txt", "w")
        f.write(song_generation(rows=5, la=10, end_of_song=1))
        print("File temp.txt was updated")
    finally:
        f.close()
    f = open("temp.txt", "r")
    print(f.read())
    f.close()

    # 2) Запись из одного файла в другой
    with open(r'/Users/itacademy/Downloads/automated_test_courses/automated_test_courses/homework_5/hw_5_task_1.py',
              encoding='UTF-8', mode='r') as f1:
        with open(r'/Users/itacademy/Downloads/automated_test_courses/automated_test_courses/homework_6/temp.txt',
                  encoding='UTF-8', mode='w') as f2:
            for line1 in f1:
                f2.write(line1)
    with open(r'/Users/itacademy/Downloads/automated_test_courses/automated_test_courses/homework_6/hw_6_task_1.py',
              encoding='UTF-8', mode='r') as f3:
        print("f2 file is", f3.read(), sep='\n')
