user_list = input('Введите значения элементов списка через запятую: ').split(',')

for i in range(1, len(user_list), 2):
    user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]

print(user_list)
