import json
import os
clear = lambda: os.system('cls')
clear()

PAHT = "sample_data/directory.txt"
clear()



def read_d():
    print()
    with open(PAHT, "r", encoding="UTF-8") as file:
        t = file.readlines()
    new_book = {}
    for i, contact in enumerate(t, 1):
        contact = contact.strip().split(";")    
        new_book[i] = {"name" : contact[0], "phone" : contact[1], "comment" : contact[2]} 
    
    for i in new_book:
        print(new_book.get(i).get("name"),"\t", new_book.get(i).get("phone"),"\t", new_book.get(i).get("comment"))
    print()
    input("Для продолжения нажми Enter ")
    clear()


def write_d():
    print()
    name = input("Введите имя контакта => ")
    tel = input("Введите телефон контакта => ")
    comment = input("Введите комментарий для контакта => ")
    temp_kontakt = name+";"+tel+";"+comment
    print(temp_kontakt)
    with open(PAHT, "a", encoding="UTF-8") as file:
        print(temp_kontakt, file=file)


def find_d():
    print("ff")


def remove_d():
    print("ff")

def edit_d():
    print()
    with open(PAHT, "r", encoding="UTF-8") as file:
        t = file.readlines()
    new_book = {}
    for i, contact in enumerate(t, 1):
        contact = contact.strip().split(";")    
        new_book[i] = {"name" : contact[0], "phone" : contact[1], "comment" : contact[2]} 
    
    for i in new_book:
        print(new_book.get(i).get("name"),"\t", new_book.get(i).get("phone"),"\t", new_book.get(i).get("comment"))
    print()
    input("Для продолжения нажми Enter ")
    clear()

while True:
    while True:
        print("Найти контакт = 1\tДобавить контакт = 2\tУдалить контакт = 3\tРедактировать контакт = 4\tПоказать весь справочник = 5\tВыход = 8")
        vibor = input("Выберите действие => ")
        if vibor.isdigit():
            vibor = int(vibor)
            break
        else:
            clear()
    if vibor == 1:
        find_d()
    elif vibor == 2:
        write_d()
    elif vibor == 3:
        remove_d()
    elif vibor == 4:
        edit_d()
    elif vibor == 5:
        read_d()
    elif vibor == 8:
        break
    else:
        clear()


