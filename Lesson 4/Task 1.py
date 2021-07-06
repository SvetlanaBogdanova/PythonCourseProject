from sys import argv


def wages(rate_per_hour, working_hours, rewards_percentage):
    try:
        return int(rate_per_hour) * int(working_hours) * (1 + int(rewards_percentage) / 100)
    except ValueError:
        print('Неверный формат данных.')


name, rate, hours, rewards = argv
worker_wage = wages(rate, hours, rewards)
print(f'Заработная плата сотрудника: {worker_wage}')
