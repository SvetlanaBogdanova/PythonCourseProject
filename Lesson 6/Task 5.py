class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def draw(self):
        print('Запуск отрисовки ручки')


class Pencil(Stationary):

    def draw(self):
        print('Запуск отрисовки карандаша')


class Handle(Stationary):

    def draw(self):
        print('Запуск отрисовки маркера')


my_stationary = Stationary('Кисть')
my_stationary.draw()
my_pen = Pen('ErichKrause')
my_pen.draw()
my_pencil = Pencil('Koh-i-Noor')
my_pencil.draw()
my_handle = Handle('Touch')
my_handle.draw()
