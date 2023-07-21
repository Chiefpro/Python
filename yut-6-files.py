
# w - write запись
# r - read чтение
# a - append дополнение

# file = open(path, flag, encoding="UTF-8")

file = open("Python/Data/file.txt", "w", encoding="UTF-8")
file.write("123")
file.close