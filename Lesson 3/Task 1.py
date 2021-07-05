def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('Деление на 0')
    except TypeError:
        print('Неверный формат аргументов. Аргументы должны быть представлены в числовом формате.')


try:
    print(division(float(input('Введите делимое: ')), float(input('Введите делитель: '))))
except ValueError:
    print('Неверный формат входных данных')
