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


class Discount:
    
    def __init__(self, value):
        if not isinstance(value, int | float):
            logger.error('Value must be a number.')
            raise ValueError('Value must be a number.')
        self._value = value
        
    def discount(self):
        return 0

class RegularDiscount(Discount):
    
    def __init__(self, value=10):
        super().__init__(value)
    def discount(self):
        return self._value

class SilverDiscount(Discount):
    
    def __init__(self, value=15):
        super().__init__(value)
    def discount(self):
        return self._value
    
class GoldDiscount(Discount):
    
    def __init__(self, value=20):
        super().__init__(value)
    def discount(self):
        return self._value