from random import randint
"""Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6"""

# z17 = []
# res = []
# size = int(input("Введи длину списка => "))
# for i in range(size):
#     z17.append(randint(0,6))
# print(*z17)
# for i in range(len(z17)):
#     if res.count(z17[i]) < 1:
#         res.append(z17[i])
# print(res)

# print(my_list := [randint(0,5) for _ in range(int(input("Веведите длину списка 2 => ")))])
# print(len(set(my_list)))

"""Задача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]"""

# print(my_list19 := [randint(0,9) for _ in range(int(input("Веведите длину списка 2 => ")))])7
# k = int(input("Введи число сдвига => "))%len(my_list19)
# my_list19 = my_list19[-k:] + my_list19[:-k]
# print(my_list19)

"""Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)"""

print(my_list23 := [randint(0, 9) for _ in range(
    int(input("Веведите длину списка 23 => ")))])
res23 = 0
for i in range(0, len(my_list23) - 1):
    if my_list23[i] < my_list23[i + 1]:
        res23 += 1
print(res23)