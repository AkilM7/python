class Trainees:

    def __init__(self, name, programs):
        self.name = name
        self.programs = programs
        
    def training(self):
        print("Practice Python")

    def lab(self):
        print(self.name, 'is practising')


trainee1 = Trainees('ajay',10)
trainee2 = Trainees('akil',15)
trainee1.training()
trainee1.lab()
