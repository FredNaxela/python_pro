import math
#Task 1

class Product:
    
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self) -> str:
        return f'{self.name.title()}({self.description}): {self.price}$'

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


#Task 3

class ProperFraction:
    
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Denominator cannot be zero.')
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        gcd = math.gcd(self.numerator, self.denominator)
        return f'{self.numerator//gcd}/{self.denominator//gcd}'

    def __mul__(self, other):
        a = self.numerator * other.numerator
        b = self.denominator * other.denominator
        return ProperFraction(a, b)
    
    def __add__(self, other):
        a = self.numerator * other.denominator + other.numerator * self.denominator
        b = self.denominator * other.denominator
        return ProperFraction(a, b)
    
    def __sub__(self, other):
        a = self.numerator * other.denominator - other.numerator * self.denominator
        b = self.denominator * other.denominator
        return ProperFraction(a, b)
    
    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator
    

try:    
    f1 = ProperFraction(1, 0)
    f2 = ProperFraction(1, 4)
except ValueError as e:
    print(e)
    
print(f1 * f2)
print(f1 + f2)
print(f1 - f2)
print(f1 == f2)