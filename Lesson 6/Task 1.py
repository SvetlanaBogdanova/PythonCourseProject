import time
from itertools import cycle


class TrafficLight:

    __colors = ('red', 'yellow', 'green', 'yellow')

    def __init__(self):
        self.__color = TrafficLight.__colors[0]

    def running(self, work_duration):
        start_time = time.perf_counter()
        for col in cycle(TrafficLight.__colors):
            if time.perf_counter() - start_time > work_duration:
                break
            if col == 'red':
                print(f'\033[30m\033[41m {col}')
                time.sleep(7)
            if col == 'yellow':
                print(f'\033[30m\033[43m {col}')
                time.sleep(2)
            if col == 'green':
                print(f'\033[30m\033[42m {col}')
                time.sleep(10)


light = TrafficLight()
light.running(22)
