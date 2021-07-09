import json

with open('text_7.txt', 'r', encoding='utf-8') as file:
    total = 0
    counter = 0
    firms_profit = {}
    for line in file:
        firm, ownership, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            total += profit
            counter += 1
        firms_profit[firm] = profit
    average_profit = {'average_profit': total / counter}
    final_list = [firms_profit, average_profit]
    print(final_list)

with open('text_7.json', 'w', encoding='utf-8') as file_j:
    json.dump(final_list, file_j, indent=4, ensure_ascii=False)
