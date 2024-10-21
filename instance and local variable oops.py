class Tour:
    
    def __init__(self,amount):
        self.amount = amount

    def shopping(self, amount):
        print("* ",self.amount)
        print("** ",amount)
        self.amount = self.amount - amount

    def eat(self):
        print("*** ",self.amount)
       # print("**** ",amount)


sakthivel = Tour(10000)
print(sakthivel.amount)
sakthivel.shopping(2000)
print(sakthivel.amount)
sakthivel.eat()
Tour.bus_fare = 1000
print(Tour.bus_fare)
