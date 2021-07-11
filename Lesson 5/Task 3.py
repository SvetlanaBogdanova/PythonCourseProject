with open('text_3.txt', 'r', encoding='utf-8') as text:
    sum_salary = 0
    number_of_workers = 0
    list_of_workers = []
    for line in text:
        number_of_workers += 1
        name, salary = line.split()
        worker_salary = float(salary)
        sum_salary += worker_salary
        if worker_salary < 20000:
            list_of_workers.append(name)
    print('Сотрудники с доходом ниже 20000:', ', '.join(list_of_workers))
    print(f'Средняя величина дохода сотрудников: {sum_salary / number_of_workers}')
