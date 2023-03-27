def power(n: int, m: int) -> int:
    if m == 0:
        return 1
    
    return n * power(n, m - 1)


n = int(input("Введите число: "))
m = int(input("Введите степень: "))
result = power(n, m)

print(f'Число "{n}" в степени "{m}" равно "{result}"')