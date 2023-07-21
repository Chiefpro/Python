import os
clear = lambda: os.system('cls')
clear()

PAHT = "sample_data/directory.txt"
clear()



def read_d():
    print()
    with open(PAHT, "r", encoding="UTF-8") as file:
        t = file.readlines()

    for i in t:
        i = i.strip().split(";")
        print(f"{i[0]}\t{i[1]}\t{i[2]}")
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
    print()
    with open(PAHT, "r", encoding="UTF-8") as file:
        t = file.readlines()
    seach_d = input("Введи имя искомого человека => ")
    dt = True
    for i in range(len(t)):
        t_lits = t[i].strip().split(";")
        if t_lits[0] == seach_d:
            print(f"{t_lits[0]}\t{t_lits[1]}\t{t_lits[2]}")
            dt = False
    if dt:
        print("Такого человека в списке нету")
    print()
    input("Для продолжения нажми Enter ")
    clear()


def remove_d():
    print()
    with open(PAHT, "r", encoding="UTF-8") as file:
        t = file.readlines()
    seach_d = input("Введи имя человека для удаления => ")
    dt = True
    for i in range(len(t)):
        t_lits = t[i].strip().split(";")
        if t_lits[0] == seach_d:
            print(f"{t_lits[0]}\t{t_lits[1]}\t{t_lits[2]}")
            dt = False
            ti = i
            while True:
                question = input("Точно удалить?\tДА = 1\tНЕТ = 0 \t=>\t")
                if question.isdigit():
                    question = int(question)
                    if question == 1 or question == 0:
                        break
                else:
                    print("Попробуйте ещё раз")
            if question == 1:
                t.pop(ti)
                tr = "".join(t)
                with open(PAHT, "w", encoding="UTF-8") as file:
                   file.write(tr)
    if dt:
        print("Такого человека в списке нету")
    
    print()
    input("Для продолжения нажми Enter ")
    clear()

def edit_d():
    print()
    with open(PAHT, "r", encoding="UTF-8") as file:
        t = file.readlines()
    seach_d = input("Введи имя человека для редактирования => ")
    dt = True
    for i in range(len(t)):
        t_lits = t[i].strip().split(";")
        if t_lits[0] == seach_d:
            print(f"{t_lits[0]}\t{t_lits[1]}\t{t_lits[2]}")
            dt = False
            ti = i
            while True:
                question = input("Что изменить?\tИмя = 1\tТелефон = 2 \tКомментарий = 3\t=>\t")
                if question.isdigit():
                    question = int(question)
                    if question == 1 or question == 2 or question == 3:
                        break
                else:
                    print("Попробуйте ещё раз")
            
            t_edit = t[ti]
            t_edit = t_edit.split(";")
            if question == 1:
                t_edit[0] = input("Введите новое имя =>\t")
            elif question == 2:
                t_edit[1] = input("Введите новый телефон =>\t")
            elif question == 3:
                t_edit[2] = input("Введите новый комментарий =>\t")
            t_edit = ";".join(t_edit)
            t[ti] = t_edit
            
            tr = "".join(t)
            
            with open(PAHT, "w", encoding="UTF-8") as file:
                file.write(tr)
    if dt:
        print("Такого человека в списке нету")
    
    print()
    input("Для продолжения нажми Enter ")
    clear()

while True:
    while True:
        print("Найти контакт = 1\tДобавить контакт = 2\tУдалить контакт = 3\tРедактировать контакт = 4\tПоказать весь справочник = 5\tВыход = 0")
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
    elif vibor == 0:
        break
    else:
        clear()


