from vehicle import Vehicle, Car

my_car = Car('Ford', 'Escape')
print(str(my_car))
print(repr(my_car))

print('\n')
print(f"my_car is type {type(my_car)}")
print(f"my_car uses {my_car.fuel}")

print(f"my_car is a Car: {isinstance(my_car, Car)}")
print(f"my_car is a Vehicle: {isinstance(my_car, Vehicle)}")
print(f"Car is a subclass of Vehicle: {issubclass(Car, Vehicle)}")