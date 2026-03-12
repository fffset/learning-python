pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
pizza['name']
'Margherita Pizza'
pizza['name'] = 'Margherita'


print(pizza['name']) # 'Margherita'

pizza.get('toppings', []) # ['mozzarella', 'basil']

pizza.keys()
# dict_keys(['name', 'price', 'calories_per_slice'])

pizza.values()
# dict_values(['Margherita Pizza', 8.9, 250])


pizza.items()
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])


pizza.clear()


pizza.pop('price', 10)
pizza.pop('total_price') # KeyError


pizza.popitem()


pizza.update({ 'price': 15, 'total_time': 25 })
"""
{
    'name': 'Margherita Pizza', 
    'price': 15, 
    'calories_per_slice': 250, 
    'toppings': ['mozzarella', 'basil'], 
    'total_time': 25
}
"""

####### LOOPING THROUGH DICTIONARIES #######
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
for price in products.values():
    print(price)

"""
990
600
250
70
"""

#keys default to looping through a dictionary, so you can also do:
for product in products.keys():
    print(product)

# Or

for product in products:
    print(product)
"""
Laptop
Smartphone
Tablet
Headphones
"""


for product in products.items():
    print(product)
"""
('Laptop', 990)
('Smartphone', 600)
('Tablet', 250)
('Headphones', 70)"""


for product, price in products.items():
    print(product, price)

"""
Laptop 990
Smartphone 600
Tablet 250
Headphones 70
"""

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

"""
{
    'Laptop': 792, 
    'Smartphone': 480, 
    'Tablet': 200, 
    'Headphones': 56
}
"""


for product in enumerate(products):
    print(product)
"""
(0, 'Laptop')
(1, 'Smartphone')
(2, 'Tablet')
(3, 'Headphones')"""