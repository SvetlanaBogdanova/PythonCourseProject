current_distance = int(input('Введите результат 1-го дня в км: '))
required_distance = int(input('Введите требуемую дистанцию в км: '))
current_day = 1

while current_distance < required_distance:
    print(f'{current_day}-й день: {current_distance:.2f} км')
    current_distance *= 1.1
    current_day += 1

print(f'{current_day}-й день: {current_distance:.2f} км')
print(f'На {current_day}-й день спортсмен достиг результата — не менее {required_distance} км.')
