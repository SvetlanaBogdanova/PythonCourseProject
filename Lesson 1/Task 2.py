time_in_sec = int(input('Введите время в сек: '))

hours = time_in_sec // 3600
minutes = (time_in_sec % 3600) // 60
seconds = time_in_sec % 60

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
