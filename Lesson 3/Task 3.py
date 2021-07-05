def sum_two(num1, num2, num3):
    try:
        return num1 + num2 + num3 - min(num1, num2, num3)
    except TypeError:
        print('Неверный формат аргументов. Аргументы должны быть представлены в числовом формате.')


try:
    result = sum_two(int(input('Первое число: ')), int(input('Второе число: ')), int(input('Третье число: ')))
    print(f'Сумма двух наибольших чисел: {result}')
except ValueError:
    print('Неверный тип данных')
