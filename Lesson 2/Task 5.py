decreased_list = [7, 5, 5, 3, 3, 3, 2, 1]

for k in range(5):
    new_elem = float(input('Введите значение нового элемента списка: '))
    for i in range(len(decreased_list) - 1, -1, -1):
        if decreased_list[i] >= new_elem:
            decreased_list.insert(i + 1, new_elem)
            break
    else:
        decreased_list.insert(0, new_elem)

print(decreased_list)
