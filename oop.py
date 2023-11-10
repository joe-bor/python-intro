# chapter_6.py

# class Car:
#     runs = True

#     def start(self):
#         if self.runs:
#             print("Car is started. Vroom vroom!")
#         else:
#             print("Car is broken :(")

# my_car = Car()
# print(f"My car runs: {my_car.runs}")
# my_car.start()


# -----

# chapter_6.py

class Car:
    runs = True
    number_of_wheels = 4

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels

    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

my_car = Car()
print(my_car)
print(type(my_car))
print(f"Cars have {Car.get_number_of_wheels()} wheels.")

# Of course, we can override this in our instance:
my_car.number_of_wheels = 6

# And when we access our new instance variable:
print(f"My car has {my_car.number_of_wheels} wheels.")

# But, when we call our class method on our instance:
print(f"My car has {my_car.get_number_of_wheels()} wheels.")

print('\n \n')

print(isinstance(my_car, Car))
print(repr(my_car))