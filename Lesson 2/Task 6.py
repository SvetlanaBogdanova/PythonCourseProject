number_of_goods = int(input('Введите количество позиций товаров для добавления: '))
goods = list()

for i in range(1, number_of_goods + 1):

    goods_name = input('Введите название товара: ')
    goods_price = float(input('Введите цену товара: '))
    goods_amount = int(input('Введите количество товара: '))
    goods_units = input('Введите ед. измерения: ')

    product = {
        'name': goods_name,
        'price': goods_price,
        'amount': goods_amount,
        'units': goods_units
    }

    goods_tuple = (i, product)
    goods.append(goods_tuple)

print(goods)

name_values = list()
price_values = list()
amount_values = list()
units_values = list()

for i in range(number_of_goods):
    name_values.append(goods[i][1].get('name'))
    price_values.append(goods[i][1].get('price'))
    amount_values.append(goods[i][1].get('amount'))
    units_values.append(goods[i][1].get('units'))

goods_analysis = {
    'name': name_values,
    'price': price_values,
    'amount': amount_values,
    'units': list(set(units_values))
}

print(goods_analysis)
