with open('text_6.txt', 'r', encoding='utf-8') as file:
    my_discipline_dict = {}
    for line in file:
        sum_hours = 0
        for el in line.split():
            if el.endswith(':'):
                discipline = el[0:el.index(':')]
            elif el != '-' and el.endswith(':') is False:
                sum_hours += int(el[0:el.index('(')])
        my_discipline_dict[discipline] = sum_hours
    print(my_discipline_dict)
