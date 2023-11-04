# print('Hello world')

# constatns dont exist in python
# convention is to ALLCAPS any CONST
# snake-case is the norm in python

# MY_CONSTANT = 5

# my_variable =  'Hello World'

# print(MY_CONSTANT)
# print(my_variable)

# ------

# Receiving Input

# user_input = input('Who are you? ')

# print(f"Hey there {user_input}")

# -----

# Conditionals

# num = 5

# if (num > 3):
#   print('Greater than 3')
# elif (num > 1):
#   print('Greater than 1')
# else:
#   print('Num is less than 1')


# ----- While Loops -----

# counter = 0

# while(counter < 10):
#   print(counter)
#   counter += 1

# ----- 10 Min Excercise -----

# counter = 0

# while (counter != 10 ):
#   if ( counter % 2 == 0):
#     print('its even')
#   elif ( counter % 3 == 0):
#     print('meow')
#   counter+=1


# ----- Collections -----

# # Lists -> arrays
# my_list = [1,2,3,'hi']
# print(my_list)
# print(my_list[0])

# # dictionary -> objects
# my_dictionary = {"cheese": "gouda", "bread": "rye"}
# print(my_dictionary)
# print(my_dictionary["cheese"])

# ----- 10 min excercise -----

my_list = [1,2,3,4,5,6,7,8,9,10]

# print(len(my_list))

# for item in my_list:
#   print(item )

# for index, item in enumerate(my_list):
#   print(f"index: {index} item: {item}")

# print(list(enumerate(['a', 'b', 'c'])))

# print(my_list.insert(1, 'a'))
# print(my_list)

# print(my_list.extend([1, 'a']))
# print(my_list)

# my_list.remove(1)
# print(my_list)

# print(my_list.pop(2))
# print(my_list)

# print(my_list.clear())
# print(my_list)

# del my_list[3:6]
# print(my_list)


# ---- Functions -----
# def add_nums (x, y):
#   return x + y

# print( add_nums(3, 6))

# subtract = lambda x, y: x - y
# print(subtract(6,5))

# def sub_nums(x, y):
#   return x - y

# def say_hello(name):
#   print(f"Hello {name}")

# print(say_hello("joe"))

# def say_hello_adv (dict):
#   print(f"Hello {dict['name']}, hows does it feel to be {dict['age']} years old")

# say_hello_adv({ "name": 'joe', 'age': 29})


# def looper(arr):
#   for item in arr:
#     print(item)

# looper([1,23,4,5])

# ----- OOP in Python -----
# class Dog:

#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def bark(self):
#     print(f"{self.name} is barking. aarrf!")


# Sparky = Dog("spark", 2)

# Sparky.bark() 


# ----- Inheritance -----
# class SmallDog(Dog):

#   def __init__ (self, name, age):
#     # super calls the constructor of the parent class
#     super().__init__(name, age)

#   #This will override the version of bark in the parent class
#   def bark(self):
#     print(f"{self.name} izzz a smalldog barking")

# Sparky = SmallDog("spark", 2)
# print(Sparky)
# Sparky.bark()


# ----- Static Methods and Properties -----
# static props/methods belong to the class, NOT the instance

class Calculator:
  # properties declared outside of the constructor are automatically static
  lastResult = 0

  @classmethod #defines this as a class method that reveive cls instead of self
  def calculate(cls, num1, num2, operator):
    cls.lastResult = eval(f"{num1} {operator} {num2} ")
    return cls.lastResult

  @staticmethod #defines this as a static method that receives neither self/cls
  def showLastResult():
    print(Calculator.lastResult)

# Calculator.calculate(2, 3, "+")
# Calculator.showLastResult()

calc_instance = Calculator()
print(calc_instance)

calc_instance.showLastResult()