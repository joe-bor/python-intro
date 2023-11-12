class Vehicle:
    
    number_of_wheels = 4
    
    def __init__(self, make, model, fuel='gas'):
        self.make = make
        self.model = model
        self.fuel = fuel
        
daily_driver = Vehicle('Ford', 'Escape')
daily_driver.number_of_wheels = 3

# number_of_wheels is a class variable
    # it exist to all instance of the class + the class itself
print(daily_driver.number_of_wheels) # 3
print(Vehicle.number_of_wheels) # 4
print('\n')

class Car(Vehicle):
    
   pass
    
class Truck(Vehicle):
    
    number_of_wheels = 6
    
    def __init__(self, make, model, fuel='diesel'):
        super().__init__(make, model, fuel)

daily_driver = Car("Subaru", "Crosstrek")
print(f"I drive a {daily_driver.make} {daily_driver.model}. "
      f"It uses {daily_driver.fuel} and has {daily_driver.number_of_wheels} wheels.")

truck = Truck("Ford", "F350")
print(f"I also have a {truck.make} {truck.model}. "
      f"It uses {truck.fuel} and has {truck.number_of_wheels} wheels.")

print(isinstance(daily_driver, Car))
print(issubclass(Car, Vehicle))

class MyException(Exception):
    def __init__(self, message):
        new_message = f"!!! ERROR !!! {message}"
        super().__init__(new_message)
        
raise MyException('Ooops')