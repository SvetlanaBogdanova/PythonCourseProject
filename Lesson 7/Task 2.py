from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def total_fabric_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def total_fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def total_fabric_consumption(self):
        return 2 * self.height / 100 + 0.3


wardrobe = [Coat(56), Coat(48), Suit(178), Coat(32), Suit(162)]
total_consumption = 0
for item in wardrobe:
    total_consumption += item.total_fabric_consumption
print(f'Общий расход ткани: {total_consumption:.2f}')
