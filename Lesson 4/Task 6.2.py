from itertools import cycle
from itertools import islice


my_list = ['Есенин', 'Горький', 'Толстой', 'Достоевский', 'Тургенев']
counter_end = int(input('Введите количество итераций: '))
for writer in islice(cycle(my_list), counter_end):
    print(writer)
