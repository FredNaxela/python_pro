class DishIterator:
    
    def __init__(self, dishes):
        self.dishes = dishes
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dishes):
            dish = self.dishes[self.index]
            self.index += 1
            return dish
        
        raise StopIteration