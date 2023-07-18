from copy import deepcopy
import random
"""Проверка на INT"""
# while True:
#     var = input("Введите число целое число: ")
#     if var.isdigit() == True:
#         var = int(var)
#         break
# print(type(var))

"""Функии текста"""

text = "eyDDDKJHtyj jet44 jkn553 333 nh52"
print(text.split())  # перевод текста в список
print(text.replace(" ", " * "))  # замена элементов
print(text.isalpha())  # проверка на STR
print(text.isdigit())  # проверка на INT
print(text.lower())  # все в нижний регистр
print(text.upper())  # все в верхний регистр
print(text.title())  # первые буквы слова в верхний регистр
print(text.capitalize())  # первая буква в строке большая
print(text.index("y"))  # находит индекс искомого эленемта
# находит индекс искомого эленемта начиная с указанного индекса
print(text.index("y", 2))
# находит индекс искомого эленемта, но если такого нету - то он вернет "-1"
print(text.find("y"))
# находит индекс искомого эленемта начиная справа, но если такого нету - то он вернет "-1"
print(text.rfind("y"))
print(text.count("y"))  # находит колличество таких совпадений
# print(text)

"""---------------------------------------------------- Срезы ---------------------------------------------------------"""

# print(start:finish:step)
print(text[12:])
print(text[12:-5])
print(text[12:-5:2])
print(text[::-1])
print(text[text.index("D"):text.index("h")])

"""Списки"""
print("----------------------------------------------------------------------------")
my_list = list()  # можно просто my_list = []
my_list_2 = my_list.copy()  # копироване списка первого уровня

my_list_3 = deepcopy(my_list)   # копирование списка целиком

for i in range(10):
    my_list.append(random.randint(0, 10))
print(my_list)

my_list.append(7)  # добавляет в конец
print(my_list)
my_list.insert(0, "начало")  # вставляет на указанную позицию
print(my_list)

my_list.insert(55, "точка Г")
my_list.insert(55, "точка Г")

my_list[4] = "жопа"  # замена указанного эллемента
print(my_list)
del_item = my_list.pop(4)  # выдергивает указанную позицию
print(my_list)
print(del_item)
my_list.remove("начало")  # удаляет указанный эллемент
print(my_list)
print(my_list.index("точка Г"))  # возвращает индекс икомого эллемента
# возвращает индекс искомого эллемента - после указанного
print(my_list.index("точка Г", 11))

g = []
for i in range(len(my_list)):
    if my_list[i] == "точка Г":
        g.append(i)
print(g)

my_list.extend([3, 4, 5])  # сложение с другим списком
print(my_list)

my_list_int = [3, 6, 3, 7, 4, 7, 2, 5, 11]
my_list_int.sort()  # сортирует список
print(my_list_int)
my_list_int.sort(reverse=True)  # сортирует список наоборот
print(my_list_int)

print(my_list.count("точка Г"))  # возвращает количество совпадений

my_list_4 = ["f", "e", "3"]
print("-".join(my_list_4))  # склеивает список в строку

my_list.clear()  # очищает список
print(my_list)

""" КОРТЕЖИ - не изиеняемы список """
print("-------------------------------------------------------")
my_turpleeeee = (3, 5, 3, "d", 6, 26, "g", 2)
print(my_turpleeeee)
print(*my_turpleeeee)  # печать без кавычек
print(*my_turpleeeee, sep="-")  # печать без кавычек, разделитель будет "-"
print(type(my_turpleeeee))

d1, d2, d3, s1, d4, d5, s2, d6 = my_turpleeeee  # распаковка кортежей
# распаковка кортежей, что не поместится запихнет в "d5"
d1, d2, d3, s1, d4, *d5 = my_turpleeeee
print(d1, d2, d3, s1, d4, d5, s2, d6)  # распаковка кортежей


"""Множества(только уникальные значения)"""
print("----------------------------------------------------------------------------")

my_list = [1, 1, 6, 3, 8, 3, 5, 6, 3, 3, 1, 1,]
my_set = set(my_list)

my_set3 = {1, 1, 6, 3, 8, 3, 5, 6, 3, 3, 1, 1, }

print(my_set)
my_set.add(9)  # добавить во множество
print(my_set)
print(type(my_set))
my_set_2 = {2, 3, 1, 7, 5}
print(my_set_2)
print(type(my_set_2))

""" Словари """
print("----------------------------------------------------------------------------")

my_dict_2 = {}
print(type(my_dict_2))
my_dict = {1: "one", 2: "two", 3: "ТРИ", 4: "ТРИ"}
print(my_dict)
my_dict[5] = "ПЯТТь"  # Добавление заначения в словарь
print(my_dict)
# возвращает значение ключа(если такого ключа нету выдаст ошибку)
print(my_dict[4])
# возвращает значение ключа(если такого ключа нету возвращает NONE)
print(my_dict.get(7))
# возвращает значение ключа(если такого ключа нету возвращает второй параметр)
print(my_dict.get(7, "нема такого ключа"))

# если такой ключ уже есть, то он не станет перзаписывать
my_dict.setdefault(2, "Два")

my_dict.update(my_dict_2)  # на my_dict накладывает my_dict_2
keys = {"one", 2, 3}
my_dict.fromkeys(keys, "пусто")  # создает словать из ключей

# ------------------------------------------------------------------------------------------------------------------------

my_list = [random.randint(1,100) for i in range(10) if not i%2] #   добавление в список рандомных значений 
print(my_list)
