def sum_numbers():
    total = 0
    num = ''
    while 'q' not in num:
        tmp = 0
        num = input('Введите числа через пробел (для выхода введите q): ').split(' ')
        for n in num:
            if n == 'q':
                break
            try:
                tmp += int(n)
            except ValueError:
                print('Неверный формат данных:', n)
        total += tmp
        print(f'{tmp}({total})')

    print(f'Итоговая сумма: {total}')


sum_numbers()
