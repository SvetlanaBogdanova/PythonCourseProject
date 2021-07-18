class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f'{self.cells}'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells < other.cells:
            raise Exception('Ошибка вычитания. Превышено количество вычитаемых ячеек')
        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, row_cells):
        cells = self.cells
        order_cells = []
        while cells > 0:
            order_cells.append(row_cells * "*" if cells >= row_cells else cells * "*")
            cells -= row_cells
        return '\n'.join(order_cells)


my_cell_1 = Cell(12)
my_cell_2 = Cell(13)

print(my_cell_1 + my_cell_2)

try:
    print(my_cell_2 - my_cell_1)
    print(my_cell_1 - my_cell_2)
except Exception as err:
    print(err)

print(my_cell_1 * my_cell_2)
try:
    print(my_cell_1 / my_cell_2)
    print(my_cell_1 / Cell(0))
except ZeroDivisionError:
    print('Деление на 0')

print(my_cell_1.make_order(4))
print(my_cell_2.make_order(3))
