class Calculator:
    def __init__(self):
        self.history = []

    def printHistory(self):
        if not self.history:
            print("No history!")
            return
        
        for i in self.history:
            print(i)

        return

    def addition(self, a, b):
        add = lambda a, b : a + b
        return add(a, b)
    
    def subtraction(self, a, b):
        sub = lambda a, b : a - b
        return sub(a, b)
    
    def multiplication(self, a, b):
        mul = lambda a, b : a * b
        return mul(a, b)
    
    def division(self, a, b):
        div = lambda a, b : a / b
        return div(a, b)