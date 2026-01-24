class Product:
    def __init__(self,name,price,brand,model):
        self.name = name
        self.price = price
        self.brand = brand
        self.model = model
product = Product('T-shirt',45,'Nike','Air Max')


attribute_check = []
attribute_check = input('Enter attributes to check (separated by commas): ').split(',')

for att in attribute_check:
    if not hasattr(product,att):
        print(f'ERROR: there is no such att called {att} ')
    else:
        print(f'{att} {getattr(product,att)}')