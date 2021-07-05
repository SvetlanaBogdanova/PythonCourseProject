revenue = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))

profit = revenue - costs  # Вычисляем прибыль

if revenue > costs:
    print('Выручка больше издержек')
    profitability = profit / revenue * 100  # Рентабельность выручки
    number_of_employees = int(input('Введите количество сотрудников: '))
    profit_per_person = profit / number_of_employees
    print(
        f'Прибыль фирмы: {profit:.2f}. '
        f'Рентабельность выручки фирмы: {profitability:.1f}%. '
        f'Прибыль фирмы в расчёте на одного сотрудника: {profit_per_person:.2f}.'
        )
elif revenue < costs:
    print(f'Издержки больше выручки. Убытки: {profit:.2f}.')
else:
    print('Выручка равна издержкам.')
