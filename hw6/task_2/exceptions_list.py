class IncorrectDiscount(Exception):
    def __init__(self, message):
        self.massage = message
    
    def __str__(self) -> str:
        return self.massage
    