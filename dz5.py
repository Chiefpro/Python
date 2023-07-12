"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """

print("------------------------------  Задача 26. -------------------------------------")

while True:
    int_a = input("Введите число А => ")
    int_b = input("Введите число В => ")
    if int_a.isdigit() and int_b.isdigit():
        int_a = int(int_a)
        int_b = int(int_b)
        break
    else:
        print("Вы ввсели не числа!!")

def exponentiate(a, b):
    if b == 0:
        return 1
    return a * exponentiate(a, b - 1)

print(f"{int_a} в степени {int_b} = {exponentiate(int_a, int_b)}")



"""Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4 """

print("------------------------------  Задача 28. -------------------------------------")

while True:
    int_a = input("Введите число А => ")
    int_b = input("Введите число В => ")
    if int_a.isdigit() and int_b.isdigit():
        int_a = int(int_a)
        int_b = int(int_b)
        break
    else:
        print("Вы ввсели не числа!!")

def rsum(a, b):
    if b == 0:
        return a
    return 1 + rsum(a, b - 1)

print(rsum(int_a, int_b))