def neg_pow(x, y):
    try:
        x, y = float(x), int(y)
        if x < 0 or y > 0:
            print('Введите действительное положительное число и целое отрицательное в качестве степени')
        else:
            return x ** y
    except ZeroDivisionError:
        print('Деление на 0')
    except ValueError:
        print('Введите числовые значения')


def neg_pow2(x, y):
    try:
        x, y = float(x), int(y)
        if x < 0 or y > 0:
            print('Введите действительное положительное число и целое отрицательное в качестве степени')
        else:
            mult = 1.0
            for _ in range(abs(y)):
                mult *= x
            return 1 / mult
    except ZeroDivisionError:
        print('Деление на 0')
    except ValueError:
        print('Введите числовые значения')


num1 = input('Введите число: ')
num2 = input('Введите степень: ')

print('Вариант с использованием оператора "*": ', neg_pow(num1, num2))
print('Вариант с циклом: ', neg_pow2(num1, num2))
