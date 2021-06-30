text = input('Введите строку: ').split()

for ind, elem in enumerate(text, 1):
    print(ind, elem[:10])
