from itertools import count

start = int(input('Начальное число: '))
end = int(input('Конечное число: '))

for num in count(start):
    if num > end:
        break
    else:
        print(num)
