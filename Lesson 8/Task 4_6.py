from abc import abstractmethod


class Warehouse:

    def __init__(self, warehouse, inventory):
        self.warehouse = warehouse
        self.inventory = inventory

    def acceptance(self, item, amount):
        article_number = item.article_number
        self.inventory.update({article_number: item})
        try:
            if self.warehouse.get(article_number) is not None:
                self.warehouse[article_number] += int(amount)
            else:
                self.warehouse.update({article_number: int(amount)})
            print(f'{amount} единиц товара {article_number} поступило на склад. '
                  f'Всего на складе: {self.warehouse[article_number]}')
        except ValueError:
            print('Неверный формат данных')

    def department_supply(self, item, amount, department_name):
        article_number = item.article_number
        try:
            if self.warehouse.get(article_number) is None:
                print('Товар отсутствует на складе')
            elif self.warehouse[article_number] < int(amount):
                print(f'Товара недостаточно на складе. Всего доступно: {self.warehouse[article_number]}')
            else:
                self.warehouse[article_number] -= int(amount)
                print(f'{amount} единиц товара {article_number} передано со склада в подразделение {department_name}. '
                      f'Остаток товара: {self.warehouse[article_number]}')
        except ValueError:
            print('Неверный формат данных')

    def get_item(self, article_number):
        return self.inventory.get(article_number)


class OfficeEquipment:

    def __init__(self, article_number, height, width, depth, model, title='Оргтехника'):
        self.article_number = article_number
        self.title = title
        self.height = height
        self.width = width
        self.depth = depth
        self.model = model

    def volume(self):
        return f'Объем упаковки {self.title} {self.model}: {self.height * self.width * self.depth}'

    @abstractmethod
    def get_parameters(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, article_number, height, width, depth, model, printer_type, speed, title='принтер'):
        super().__init__(article_number, height, width, depth, model, title)
        self.printer_type = printer_type
        self.speed = speed

    @property
    def get_parameters(self):
        return f'Параметры принтера {self.model}: ' \
               f'вид принтера - {self.printer_type}, ' \
               f'скорость печати - {self.speed}'


class Scanner(OfficeEquipment):

    def __init__(self, article_number, height, width, depth, model, sensor_type):
        super().__init__(article_number, height, width, depth, model, title='сканнер')
        self.sensor_type = sensor_type

    @property
    def get_parameters(self):
        return f'Параметры сканнера {self.model}: ' \
               f'тип сенсора - {self.sensor_type}'


class Xerox(Printer):

    def __init__(self, article_number, height, width, depth, model, printer_type, speed, type_of_printing):
        super().__init__(article_number, height, width, depth, model, printer_type, speed, title='ксерокс')
        self.type_of_printing = type_of_printing

    @property
    def get_parameters(self):
        return f'Параметры ксерокса {self.model}: ' \
               f'вид ксерокса - {self.printer_type}, ' \
               f'скорость печати - {self.speed}, ' \
               f'тип печати - {self.type_of_printing}'


class Menu:

    def __init__(self, warehouse):
        self.stop = False
        self.warehouse = warehouse

    def start(self):
        while not self.stop:
            self.main_menu()

    def main_menu(self):
        print('\n [1] Просмотреть информацию о товаре')
        print(' [2] Добавить на склад')
        print(' [3] Передать в подразделение')
        print(' [4] Создать новый товар')
        print(' [5] Выход')

        action = input('\nВаш выбор: ')

        if action == '5':
            self.stop = True
        elif action == '1':
            self.item_info()
        elif action == '2':
            self.add_item()
        elif action == '3':
            self.move_item()
        elif action == '4':
            self.create_item()
        else:
            print('Выберите пункт меню из предложенных')

    def item_info(self):
        article = input('Введите артикул товара: ')
        item = self.warehouse.get_item(article)
        if item is not None:
            print(item.get_parameters)
        else:
            print('Артикул не найден')

    def add_item(self):
        article = input('Введите артикул товара: ')
        item = self.warehouse.get_item(article)
        if item is not None:
            amount = input('Введите количество ед. товара: ')
            self.warehouse.acceptance(item, amount)
        else:
            print('Артикул не найден')

    def move_item(self):
        article = input('Введите артикул товара: ')
        item = self.warehouse.get_item(article)
        if item is not None:
            amount = input('Введите количество ед. товара: ')
            department = input('Введите подразделение: ')
            self.warehouse.department_supply(item, amount, department)
        else:
            print('Артикул не найден')

    def create_item(self):

        print('\nВыберите тип товара: ')
        print(' [1] Принтер')
        print(' [2] Сканер')
        print(' [3] Ксерокс')
        print(' [4] Назад')

        action = input('\nВаш выбор: ')

        if action == '4':
            return
        elif action == '1':
            self.create_printer()
        elif action == '2':
            self.create_scanner()
        elif action == '3':
            self.create_xerox()
        else:
            print('Выберите пункт меню из предложенных')

    def create_printer(self):
        article_number = input('Введите артикул принтера: ')
        item = self.warehouse.get_item(article_number)
        if item is not None:
            print('Товар с таким артикулом уже существует')
            return
        height = input('Введите высоту упаковки: ')
        width = input('Введите ширину упаковки: ')
        depth = input('Введите глубину упаковки: ')
        model = input('Введите модель принтера: ')
        printer_type = input('Введите тип принтера: ')
        speed = input('Введите скорость печати принтера: ')
        new_printer = Printer(article_number, height, width, depth, model, printer_type, speed)
        self.warehouse.inventory.update({article_number: new_printer})
        print('Товар успешно добавлен')

    def create_scanner(self):
        article_number = input('Введите артикул сканнера: ')
        item = self.warehouse.get_item(article_number)
        if item is not None:
            print('Товар с таким артикулом уже существует')
            return
        height = input('Введите высоту упаковки: ')
        width = input('Введите ширину упаковки: ')
        depth = input('Введите глубину упаковки: ')
        model = input('Введите модель сканнера: ')
        sensor_type = input('Введите тип сенсора: ')
        new_scanner = Scanner(article_number, height, width, depth, model, sensor_type)
        self.warehouse.inventory.update({article_number: new_scanner})
        print('Товар успешно добавлен')

    def create_xerox(self):
        article_number = input('Введите артикул ксерокса: ')
        item = self.warehouse.get_item(article_number)
        if item is not None:
            print('Товар с таким артикулом уже существует')
            return
        height = input('Введите высоту упаковки: ')
        width = input('Введите ширину упаковки: ')
        depth = input('Введите глубину упаковки: ')
        model = input('Введите модель ксерокса: ')
        xerox_type = input('Введите тип ксерокса: ')
        speed = input('Введите скорость печати ксерокса: ')
        type_of_printing = input('Введите тип печати ксерокса: ')
        new_xerox = Xerox(article_number, height, width, depth, model, xerox_type, speed, type_of_printing)
        self.warehouse.inventory.update({article_number: new_xerox})
        print('Товар успешно добавлен')


printer_1 = Printer('121', 50, 100, 50, 'Epson 2310', 'jet', 200)
printer_2 = Printer('110', 40, 80, 30, 'Epson 23M', 'jet', 300)
scanner = Scanner('122A', 40, 80, 30, 'Epson 510', 'CIS')
xerox = Xerox('134', 100, 120, 60, 'HP LaserJet 23P', 'laser', 300, 'colored')

warehouse = Warehouse({'110': 1, '121': 4, '134': 3}, {'121': printer_1, '122A': scanner, '134': xerox, '110': printer_2})
menu = Menu(warehouse)
menu.start()
