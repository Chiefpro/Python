"""Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2"""

input_string = "aaabcaadcdd"
char_count = {}
output = []

for char in input_string:
    if char in char_count:
        char_count[char] += 1
        output.append(f"{char}_{char_count[char]}")
    else:
        char_count[char] = 0
        output.append(char)
output_string = ' '.join(output)
print(output_string)


# input_string = list(input_string)
# res25 = []
# print(input_string)
# for i in input_string:
#     k=0
#     for j in range(len(input_string)):
#         if i == input_string[j]:
#             k +=1
#         if k == 0:
#             res25.append(input_string[j])
#         else:
#             res25.append(k)
    
# print(res25)

"""--------------------Задача №27. Решение в группах----------------------"""

import re
Input27 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
delimiters = r"[. ]+"
res = re.split(delimiters, Input27)
print(res)
print(len(res))

"""--------------------Задача №27. Решение в группах----------------------"""

