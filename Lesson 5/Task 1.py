with open("result_1.txt", "w", encoding="utf-8") as file:
    user_data = input('Запись: ')
    while user_data != '':
        file.write(f'{user_data}\n')
        user_data = input('Следующая запись (для выхода - введите пустую строку): ')
