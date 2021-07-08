def user_profile(name, surname, year_of_birth, city, email, phone):
    print(f'Данные о пользователе: {name} {surname}, город {city}, {year_of_birth} года рождения. '
          f'e-mail: {email}, телефон {phone}')


try:
    user_profile(name=input('Введите Ваше имя: '), surname=input('Введите Вашу фамилию: '),
                 year_of_birth=int(input('Год рождения: ')), city=input('Город проживания: '),
                 phone=input('Номер телефона: '), email=input('Адрес электронной почты: '))
except ValueError:
    print('Неверный формат данных')
