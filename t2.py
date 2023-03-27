from random import randint


def sum(a: int, b: int) -> int:
    if b == 0:
        return a
    elif a == 0:
        return b
    
    return a + sum(1, b - 1)


a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))

print(sum(a, b))