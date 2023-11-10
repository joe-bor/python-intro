# chapter_6.py

class Car:
    runs = True

    # called upon instantiation of object
    def __init__(self, make, model):
        self.make = make
        self.model = model

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
    

my_car = Car("Ford", "Thunderbird")
# my_car.start()
# print(f"This object is a {str(my_car)}")
print("\n")
print(str(my_car))
print(repr(my_car))


# Python repl
'''
>>> import datetime
>>> now = datetime.datetime.now()
>>> str(now)
'2023-11-10 03:07:24.435722'
>>> repr(now)
'datetime.datetime(2023, 11, 10, 3, 7, 24, 435722)'
>>> 
'''