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