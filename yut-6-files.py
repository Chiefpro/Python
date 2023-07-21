
# w - write запись
# r - read чтение
# a - append дополнение

# file = open(path, flag, encoding="UTF-8")

file = open("Python/Data/file.txt", "w", encoding="UTF-8")
file.write("123")
file.write("abc\n")
file.write("Новая\nстрока")
file.close

file = open("Python/Data/file.txt", "a", encoding="UTF-8")
file.write(" дописать что-то")
file.close

file = open("Python/Data/file.txt", "r", encoding="UTF-8")
data_line = file.readline() # считывание построчно
data = file.read()
file.close
print(data)
print(type(data))

my_list = [data]
print(my_list)

print(data_line)

# _-------------------------

file = open("Python/Data/file.txt", "r", encoding="UTF-8")
data = file.readlines() # запихивает в список
file.close
print(data)
print(type(data))


#  ======================================================================================================
print("==============================================================")

with open("Python/Data/file.txt", "a", encoding="UTF-8") as file:
    print(' Фифифифи', file=file)


with open("Python/Data/file.txt", "r", encoding="UTF-8") as file:
    data_list = []
    data_list = file.readline()

print(data_list)

#  ======================================================================================================
print("==============================================================")

with open("Python/Data/directory.txt", "r", encoding="UTF-8") as file:
    phone_book = file.readlines()

print(phone_book)
new_book = {}
for i, contact in enumerate(phone_book, 1):
    contact = contact.strip().split(";")    #strip - очищает от символов(спец символов)
    new_book[i] = {"name" : contact[0], "phone" : contact[1], "comment" : contact[2]}    

print(new_book)
print("---------------------------------------")
print(new_book.get(1).get("name" ))

# --------------------------------------    JSON    ------------------------------------
print("# --------------------------------------    JSON    ------------------------------------")

import json

JSON_PATH = "Python/data/text.json"
with open(JSON_PATH, "w", encoding="UTF-8") as file:
    json.dump(new_book, file )  # записть в фаил с сохранинием типа данных

with open(JSON_PATH, "r", encoding="UTF-8") as file:
    json_data = json.load(file) # прочитать из файла с сохранинием типаданных

print(json_data)