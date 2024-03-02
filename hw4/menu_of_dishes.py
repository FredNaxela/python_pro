import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(console_handler)



class Dish:
    
    def __init__(self, name, description, price):
        if not isinstance(price, int | float):
            logger.error('Price must be a number.')
            raise TypeError('Price must be a number.')
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} ({self.description}) - {self.price}$'
    

class MenuCategory:
    
    def __init__(self, name):
        self.name = name
        self.dishes = []
        
    def add_dish(self, dish):
        if not isinstance(dish, Dish):
            logger.error('Dish must be a Dish object.')
            raise TypeError('Dish must be a Dish object.')
        self.dishes.append(dish)
        logger.info(f'Added to menu {dish}')
        
    def __str__(self):
        return f'{self.name}:\n\t{'\n'.join(map(str, self.dishes))}'