"""
Задание 1
Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла.
"""
import re


def string_matching(first_file, second_file):
    file_1 = open(f"{first_file}", "r", encoding="utf-8")
    first_file = f"{file_1.read()}"
    file_1.close()

    file_2 = open(f"{second_file}", "r", encoding="utf-8")
    second_file = f"{file_2.read()}"
    file_2.close()

    if first_file == second_file:
        print("Строки равны")
    else:
        split_first_file = first_file.split("\n")
        split_second_file = second_file.split("\n")
        for idx, i in enumerate(split_first_file):
            if i != split_second_file[idx]:
                print(f"Не равна строка: {split_second_file[idx]}")


file_1_read = "Task_1/file_1"
file_2_read = "Task_1/file_2"
string_matching(file_1_read, file_2_read)

"""
Задание 2
Дан текстовый файл. Необходимо создать новый файл
и записать в него следующую статистику по исходному
файлу:
    Количество символов;
    Количество строк;
    Количество гласных букв;
    Количество согласных букв;
    Количество цифр.
"""


def statistics(path_file_name):
    with open(f"{path_file_name}", "r", encoding="utf-8") as infile:
        lines = 0
        words = 0
        characters = 0
        count_vowels = 0
        count_consonants = 0
        digits = []
        regex = r'^[0-9]*[.,]?[0-9]+$'
        regex_digits = re.compile(regex)

        for line in infile:
            words_list = line.split()
            lines = lines + 1
            words = words + len(words_list)
            for word in words_list:
                digit = ''.join([char for char in word if regex_digits.findall(char)])
                if digit:
                    digits.append(float(digit))
                for i in range(0, len(word)):
                    if word[i] in "аиеёоуыэюя":
                        count_vowels += 1
                    else:
                        count_consonants += 1
            characters += sum(len(word) for word in words_list)
    infile.close()

    info = f"Количество символов: {characters}\n" \
           f"Количество строк: {lines}\n" \
           f"Количество гласных букв: {count_vowels}\n" \
           f"Количество согласных букв: {count_consonants}\n" \
           f"Количество цифр: {len(digits)}"
    file_info = open('Task_2/answer.txt', 'w', encoding="utf-8")
    file_info.write(info)
    file_info.close()


path_2 = "Task_2/file_for_second_task"
statistics(path_2)

"""
Задание 3
Дан текстовый файл. Удалить из него последнюю
строку. Результат записать в другой файл.
"""


def delete_last_line(path_file_name):
    with open(f"{path_file_name}", "r", encoding="utf-8") as infile, \
            open('Task_3/outfile.txt', 'w', encoding="utf-8") as outfile:
        lines = [line for line in infile]
        lines.pop()
        outfile.writelines(lines)
    infile.close()
    outfile.close()


path_3 = "Task_3/infile.txt"
delete_last_line(path_3)

"""
Задание 4
Дан текстовый файл. Найти длину самой длинной
строки.
"""


def file_length(path_file_name):
    with open(f"{path_file_name}", "r", encoding="utf-8") as infile:
        max_length = 0
        for line in infile:
            if len(line) > max_length:
                max_length = len(line) - 1
        print(f"Длина самой длинной строки: {max_length}")


path_4 = "Task_4/file.txt"
file_length(path_4)

"""
Задание 5
Дан текстовый файл. Посчитать сколько раз в нем
встречается заданное пользователем слово.
"""


def search_word(word):
    with open("Task_5/file.txt", "r", encoding="utf-8") as infile:
        count_of_word = 0
        for line in infile:
            line_split = line.split()
            for i in range(0, len(line_split)):
                if word in line_split[i]:
                    count_of_word += 1
        print(count_of_word)


users_word = input("Введите слово: ")
search_word(users_word)

"""
Задание 6
Дан текстовый файл. Найти и заменить в нем задан-
ное слово. Что искать и на что заменять определяется
пользователем.
"""


def replacement_word(word, replace):
    with open('Task_6/file.txt', "r", encoding="utf-8") as file_in:
        text = file_in.read()

    text = text.replace(word, replace)

    with open('Task_6/file.txt', "w", encoding="utf-8") as file_out:
        file_out.write(text)


users_word = input("Введите слово: ")
users_replace = input("Введите слово, на которое хотите заменить: ")
replacement_word(users_word, users_replace)
