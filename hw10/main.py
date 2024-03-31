from abc import ABC, abstractmethod

#Task 1
class BalanceDescriptor:
    
    def __init__(self, attr):
        self.balance = attr

    def __get__(self, instance, owner):
        return self.balance

    def __set__(self, instance, value):
        raise AttributeError("Modification of balance is not allowed")


class Account:
    
    def __init__(self, balance):
        self._balance = balance
        
    balance = BalanceDescriptor("balance")

    @property
    def balance(self):
        return self._balance

    def __setattr__(self, key, value):
        if key == "balance":
            raise AttributeError("Modification of balance is not allowed")
        super().__setattr__(key, value)

    def __getattr__(self, key):
        if key == "balance":
            return "Balance attribute does not exist"
        raise AttributeError(f"Class has no attribute {key}")
     

x = Account(5)
print(x._balance)

try:
    x.balance = 10
except AttributeError as e:
    print("AttributeError:", e) 
    
try:
    print(x.test)
except AttributeError as e:
    print("AttributeError:", e)


#Task 2
class User:
    
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    def __setattr__(self, key, value):
        if key in ['first_name', 'last_name']:
            raise AttributeError("Modification of 'first_name' and 'last_name' is not allowed.")
        super().__setattr__(key, value)
    
    def __getattr__(self, key):
        return f"Class has no attribute {key}"


x = User("Ivan", "Ivanov")

try:
    x.first_name = "Alex"
except AttributeError as e:
    print("AttributeError:", e)
    
print(x.age)


#Task 3
class Rectangle:
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    def __setattr__(self, key, value):
        if key in ['width', 'height']:
            raise AttributeError("Modification of 'width' and 'height' is not allowed.")
        super().__setattr__(key, value)
    
    def __getattr__(self, key):
        return f"Class has no attribute {key}"
    
    def area(self):
        return self._width * self._height
    

x = Rectangle(2, 3)

try:
    x.width = 5
except AttributeError as e:
    print("AttributeError:", e)
    
print(x.test)

print(x.area())


#Task 4
import math

class Figure(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3


circle = Circle(2)
rectangle = Rectangle(3, 4)
triangle = Triangle(2, 3, 4)

print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())


#Task 5
class PaymentMethod(ABC):
    
    @abstractmethod
    def make_payment(self, amount):
        pass


class CreditCard(PaymentMethod):
    
    def make_payment(self, amount):
        print(f"Payment of {amount}$ made by credit card")
        

class BankTransfer(PaymentMethod):
    
    def make_payment(self, amount):
        print(f"Payment of {amount}$ made by bank transfer")
        

class EWallet(PaymentMethod):
    
    def make_payment(self, amount):
        print(f"Payment of {amount}$ made by e-wallet")
        

class PaymentProcessor:
    
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, payment_method):
        self.payment_methods.append(payment_method)

    def process_payment(self, amount, payment_method):
        if payment_method in self.payment_methods:
            payment_method.make_payment(amount)
        else:
            print("Invalid payment method")


credit_card = CreditCard()
bank_transfer = BankTransfer()
e_wallet = EWallet()

payment_processor = PaymentProcessor()
payment_processor.add_payment_method(credit_card)
payment_processor.add_payment_method(bank_transfer)
payment_processor.add_payment_method(e_wallet)

payment_processor.process_payment(100, credit_card) 
payment_processor.process_payment(200, bank_transfer)  
payment_processor.process_payment(300, e_wallet) 
