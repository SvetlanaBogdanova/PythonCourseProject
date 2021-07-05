number = input('Введите число: ')

while int(number) < 0:
    print('Введите число больше 0.')
    number = input('Введите число: ')

number2 = number * 2
number3 = number * 3

print(int(number) + int(number2) + int(number3))
