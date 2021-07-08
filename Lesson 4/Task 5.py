from functools import reduce


def multiplier(arg1, arg2):
    return arg1 * arg2


result_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(multiplier, result_list[:]))
