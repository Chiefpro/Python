from random import randint


def input_int(a, b):
    while True:
        n = input(a)
        if n.isdigit():
            n = int(n)
            return n
        else:
            print(b)

def fill_list(n):
    list1 = []
    for i in range(0, n):
        list1.append(randint(1, 30))
    return list1

"""Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

print("----------------------------- Задача 30. ----------------------------")

a1 = input_int("Введите первый элемент => ", "Вы ввели не число!!!")
d1 = input_int("Введите разрядность => ", "Вы ввели не число!!!")
n1 = input_int("Введите колличество элементов => ", "Вы ввели не число!!!")

list30 = []
list30.append(a1)
for i in range(1, n1):
    list30.append(list30[i-1] + d1)
print(list30)

"""Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)"""

print("----------------------------- Задача 32. ----------------------------")

len_list = input_int("Введите длину списка => ", "Вы ввели не число!!!")
list32 = fill_list(len_list)
print(list32)
min30 = input_int("Введите минимальную границу диапозона => ", "Вы ввели не число!!!")
max30 = input_int("Введите максимальную границу диапозона => ", "Вы ввели не число!!!")
range_list = []
for i in range(len(list32)):
    if list32[i] >= min30 and list32[i] <= max30:
        range_list.append(i)
print(range_list)