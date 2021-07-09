from random import randint

with open('task_5.txt', 'w+') as file:
    numbers = [str(randint(1, 1001)) for _ in range(10)]
    file.write(' '.join(numbers))

    file.seek(0)
    nums = file.readline().split()
    total = 0
    for num in nums:
        total += int(num)
    print(f'Сумма чисел в файле: {total}')
