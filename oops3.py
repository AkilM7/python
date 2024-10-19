class Tour:
    
    def __init__(self,amount):
        self.amount = amount

    def shopping(self, amount):
        self.amount = self.amount - amount


sakthivel = Tour(10000)
print(sakthivel.amount)
sakthivel.shopping(2000)
print(sakthivel.amount)
