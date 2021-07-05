number = int(input('Введите число: '))
max_number = 0

while number > 0:
    n = number % 10
    if n > max_number:
        max_number = n
        if max_number == 9:
            break
    number //= 10

print(max_number)
