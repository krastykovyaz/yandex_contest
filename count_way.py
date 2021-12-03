# D. Задача 4.

# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Условие Дан массив, состоящий из букв 'X', 'Y' и 'O'. Необходимо найти кратчайшее расстояние между буквами 'X' и 'Y', либо вывести 0, если 'X' либо 'Y' отсутствуют. Примечания дистанция между двумя рядом стоящими буквами считается как 1 (одно межбуквенное расстояние) дистанция может считаться в обе стороны
# Пример входного файла input.txt
# "OOOXOOYOXO"
# Пример выходного файла output.txt
# 2

import sys

# with open('input.txt', 'r') as f:
#     string = f.read()

string = input()

if 'Y' not in string or 'X' not in string:
	print(0)
	sys.exit(0)

# print(string)

x_i = -1
min_len = 10**10
last_char = None
for i in range(len(string)):

    char = string[i]

    if char == 'X':
        x_i = i
        # print(i, 'X')
        # print('x_i', x_i)
        continue
    if char == 'O':
        # print(i, 'O')
        continue
    if char == 'Y':
        # print(i, 'Y')
        if x_i == -1:
            continue
        min_len = min(min_len, i - x_i)
        # print("min_len: ", min_len)

x_i = -1
for i in range(len(string)):

    char = string[i]

    if char == 'Y':
        x_i = i
        # print(i, 'Y')
        # print('y_i', x_i)
        continue
    if char == 'O':
        # print(i, 'O')
        continue
    if char == 'X':
        # print(i, 'X')
        if x_i == -1:
            continue
        min_len = min(min_len, i - x_i)
        # print("min_len: ", min_len)

print(min_len)
