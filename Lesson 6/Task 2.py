class Road:

    weight_per_meter = 25

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self.thickness = thickness

    def weight(self):
        print(f'Масса асфальта: {(self._length * self._width * Road.weight_per_meter * self.thickness) / 1000} т')


def get_road_parameters():
    length = int(input('Введите длину дороги в м: '))
    width = int(input('Введите ширину дороги в м: '))
    thickness = int(input('Введите толщину полотна в см: '))
    return length, width, thickness


my_road_1 = Road(*get_road_parameters())
my_road_1.weight()
