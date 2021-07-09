with open('result_1.txt', 'r', encoding='utf-8') as file:
    counter_lines = 0
    for line in file:
        counter_lines += 1
        print(f'В {counter_lines}-й строке: {len(line.split())} слова')
print(f'Всего в файле: {counter_lines} строк')
