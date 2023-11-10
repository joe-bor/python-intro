
class Vehicle:
    
    def __init__(self, make, model, fuel='gas'):
        self.make = make
        self.model = model
        self.fuel = fuel
        
class Car(Vehicle):
    
    def __init__(self, make, model, fuel='gas'):
        super().__init__(make, model, fuel)
        
    # maps to str()
    # should return a readable end-user output
    def __str__(self):
        return f"<<Car object: {self.make} {self.model}>>"

    #maps to repr()
    # should return Python code necessary to rebuild the object
    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"
    
    def start(self):
        if self.runs:
            print(f"Your {self.make} {self.model} is started. Vroom vroom!")
        else:
            print(f"Your {self.make} {self.model} is broken :(")