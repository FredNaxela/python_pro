import math

class Product:
    
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self) -> str:
        return f'{self.name.title()}({self.description}): {self.price}$'
    
    
class CartIterator:
    
    def __init__(self, products):
        self.products = products
        self.item = list(self.products.items())
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index < len(self.item):
            res = self.item[self.index]
            self.index += 1
            return res
        
        raise StopIteration
        
    
class Cart:
    
    def __init__(self):
        self.products = {}

    def add_products(self, product:Product, amount):
        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount
    
    def total_price(self):
        total = 0
        for product, amount in self.products.items():
           total += product.price * amount
        return total 
        
    def __str__(self) -> str:
        res = "\n".join([f'{product} - amount: {amount}' for product, amount in self.products.items()])
        return f'{res} \nTotal price: {self.total_price()}$'
    
    def __iadd__(self, other):
        for product, amount in other.products.items():
            self.add_products(product, amount)
        return self

    def __iter__(self):
        return CartIterator(self.products)
        

customer_cart1 = Cart()
customer_cart2 = Cart()

p1 = Product('borjomi','water', 2)
p2 = Product('milka','candy', 3)
p3 = Product('tabasco','souse', 4)
p4 = Product('kozel','beer', 1)

customer_cart1.add_products(p1, 2)
customer_cart1.add_products(p2, 3)
customer_cart1.add_products(p3, 1)

customer_cart2.add_products(p4, 2)
customer_cart2.add_products(p1, 1)
customer_cart2.add_products(p3, 3)

customer_cart1 += customer_cart2
print(customer_cart1)

for res, amount in customer_cart1:
    print(f'{res} - amount: {amount}')