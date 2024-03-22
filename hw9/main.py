class Cart:
    
    def __init__(self, products, quantities) -> None:
        self.products = products
        self.quantities = quantities
    
    @property
    def products(self):
        return self.__products
    
    @property
    def quantities(self):
        return self.__quantities
    
    @products.deleter
    def products(self):
        raise AttributeError("You cant delete product")
    
    @quantities.deleter
    def quantities(self):
        raise AttributeError("You cant delete quantities")
    
    def __str__(self) -> str:
        return f"{self.products} {self.quantities}"
    
    