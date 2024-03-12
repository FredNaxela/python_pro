import exceptions_list
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


class Client:
    
    def __init__(self, name, discount):
        self.name = name
        if discount.discount() < 0 or discount.discount() > 100:
            logger.error('Discount must be between 0 and 100.')
            raise exceptions_list.IncorrectDiscount('Discount must be between 0 and 100.')
        self.discount = discount
        logger.debug(f'Discount {discount.discount()}% applied client {name}.')
    
    def get_total_price(self, order):
        total_price = 0
        for dish in order:
            total_price += dish.price
        return total_price * (1 - self.discount.discount() / 100)
        
    def __str__(self):
        return self.name