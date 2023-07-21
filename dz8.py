import json
PAHT = "Python/sample_data/directory.txt"


def read_d():
    print("ff")
    # with open(PAHT, "w", encoding="UTF-8") as file:


def write_d():
    print("ff")
    # with open(PAHT, "w", encoding="UTF-8") as file:
    #     name = input("Введите имя контакта => ")
    #     tel = input("Введите телефон контакта => ")
    #     comment = input("Введите комментарий для контакта => ")

def find_d():
    print("ff")


def remove_d():
    print("ff")

while True:
    print("Найти контакт = 1\tДобавить контакт = 2\tУдалить контакт = 3\tВыход = 4")
    vibor = input("Выберите действие => ")
    vibor = int(vibor)
    if vibor == 1:
        find_d()
    elif vibor == 2:
        write_d()
    elif vibor == 3:
        remove_d()
    elif vibor == 4:
        break


