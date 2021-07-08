def fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
        yield total


num = int(input('Задайте число: '))
for el in fact(num):
    print(el)
