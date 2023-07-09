from random import randint

"""Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
Пример:
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""
print("--------------------------------- Задача 22 ----------------------------------")
while True:
    len_list_1 = input("Введите длину первого списка => ")
    len_list_2 = input("Введите длину второго списка => ")
    if len_list_1.isdigit() and len_list_2.isdigit():
        len_list_1 = int(len_list_1)
        len_list_2 = int(len_list_2)
        break
    else:
        print("Вы ввсели не числа!!")
list_22_1 = []
list_22_2 = []
for i in range(len_list_1):
    list_22_1.append(randint(1, 10))
for i in range(len_list_2):
    list_22_2.append(randint(1, 10))

print(list_22_1)
print(list_22_2)
print("--------- Сортировка ---------")
list_22_1 = set(list_22_1)
list_22_2 = set(list_22_2)
list_22_1 = list(list_22_1)
list_22_2 = list(list_22_2)
print(list_22_1)
print(list_22_2)

list_find = []

for i in range(len(list_22_1)):
    for j in range(len(list_22_2)):
        if list_22_1[i] == list_22_2[j]:
            list_find.append(list_22_1[i])
print(list_find)


"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена
система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
Пример:
4 -> 1 2 3 4
9
"""

print("--------------------------------- Задача 24 ----------------------------------")