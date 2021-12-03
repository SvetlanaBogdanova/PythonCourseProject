class ZeroDivisionErr(Exception):

    def __init__(self, num):
        super().__init__(f'Деление на ноль числа {num}')


def divide(num1, num2):
    try:
        if num2 == 0:
            raise ZeroDivisionErr(num1)
        return int(num1) / int(num2)
    except ZeroDivisionErr as error:
        print(error)


divide(64, 0)
