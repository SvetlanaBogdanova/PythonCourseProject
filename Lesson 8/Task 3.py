class IsNotDigitError(Exception):

    def __init__(self, num):
        super().__init__(f'{num} - не число!')


def isdigit():
    numbers = []
    while True:
        num = input('Введите число (для выхода введите q): ')
        if num == 'q':
            break
        try:
            if not num.isdigit():
                raise IsNotDigitError(num)
            numbers.append(int(num))
        except IsNotDigitError as error:
            print(error)

    print(f'Итоговый список: {numbers}')


isdigit()
