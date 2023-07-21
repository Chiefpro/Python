from typing import Callable # добавление типа функции

def change_num(num: int, name: str) -> str:     #   анотация принимаемых аргументов
    num *= 10
    num //= 5
    return f"Новое число {name} - {num}"

print(change_num(10, "Большое число"))

def change_num_2(num: int, name: str = "ПО УМОЛЧАНИЮ") -> str:     #   задание аргумента по умолчанию
    num *= 10
    num //= 5
    return f"Новое число {name} - {num}"

print(change_num_2(10, "Большое число"))

def change_num_3(num: int, *args, **kwargs) -> int:     # аргумент который может и гне задаваться
    num *= 10
    if args:
        num *= int(args[0])
    return num

print(change_num_3(10,))
print(change_num_3(10, 10))

# ----------------------------------- lambda ----------------------------------------

my_list = [234, 226, 23, 56]
lambda a: my_list.count(a)

def operation(func, a, b):
    return func(a,b)

print(operation((lambda a,b: a+b), 4, 5))

# ----------------------------------- Функции высшего порядка ----------------------------------------

# ***************     map     ******************
print("***************     map     ******************")

string = "12356839"
num_list = list(string)
print(num_list)

# for i in range(len(num_list)):
#     num_list[i] = int(num_list[i])

num_list = list(map(int, num_list))
print(num_list)

num_list = list(map(lambda x: x * 10, num_list))
print(num_list)

# ***********    filter     ***********
print("***********    filter     ***********")

num_list = list(filter(lambda x: int(x)%3 == 0, num_list))
print(num_list)

string_2 = "388fb895nb3893bbk3"
string_2 = list(string_2)
print(string_2)
string_2 = list(filter(lambda x: x.isdigit(), string_2))
print(string_2)

# ***********    enumerate     ***********
print("***********    enumerate     ***********")

n_list = [i for i in "hbjbksjbglw"]
print(n_list)

for i in enumerate(n_list):
    print(i)

for i, letter in enumerate(n_list, 20):
    print(i, letter)

# ***********    zip     ***********
print("***********    zip     ***********")

a_list = [i for i in "hjkbkjbkakbkljbaaa"]
b_list = [i for i in "234567898765432"]
c_list = [i for i in "#$%^*(^&$*())"]

print(a_list)
print(b_list)
print(c_list)
print("----------------------------------------------------")

new_list = list(zip(a_list, b_list, c_list))    #склеивает в кортежи
print(new_list)

print("--------------------------------------------------")

from itertools import zip_longest

new_list_2 = list(zip_longest(a_list, b_list, c_list, fillvalue='Пусто'))    #склеивает в кортежи
print(new_list_2)

