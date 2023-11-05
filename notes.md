# Python Notes

very unstructured and random notes I take while learning Python, a lot of comparisons to JS as it is the language I am comfortable with

## Multiple Assignments

- this also works if assigning diff data types

```py
a, b, c, d = 1, 2, "3", ["x", "z"]

print(a) # 1
print(b) # 2
print(c) # 3 (string)
print(d) # ["x", "z"]
```

## List Comprehensions

- dig DEEPER on this one in the future
- basically 1 liner for simple list transformations

```py
# creates a list[] of 1-10 raised to the power of 2
squares = [x**2 for x in range(1,11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares) # [4, 16, 36, 64, 100]

```

## Slicing

- built-in slicing for lists and strings

```py
my_list =  [1, 2, 3, 4, 5]
first_three = my_list[:3]
print(first_three) # [1, 2, 3]
```

## Destructuring Assignments

- swap values w/o using a temp variable

```py
a, b = b, a
```

- extract values from data structures

```py
coordinates = (3, 4)
x, y = coordinates

print(x, y) # 3 4
```

## Default ARgument Values

```py
def greet(name="Guest")
    print(f"Hello {name}")

greet()  # Prints "Hello, Guest!"
greet("Alice")  # Prints "Hello, Alice!"
```

## String formatting

- equivalent to JS template literals

```py
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

person = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}
message = f"Hello, my name is {person['name']}. I am {person['age']} years old, from {person['city']}.

```

## Generators

- chatgpt: "Python allows you to create generators, which are a way to generate values on the fly without storing them in memory. This is useful for iterating over large datasets."

- look into this in the future

## Pythonic Idioms

- What is considered "Pythonic"
- focus on readability and simplicity
- ie. list comprehension vs explicit loops

---

# Functions

## Naming conventions

    function names -> snake_case
    function arguments -> lowercase, underscores
    private functions -> prefix the function's name with an underscore
    module-level functions -> include a description

```py
def calculate_total_cost(item_price, quantity):
    """
    Calculate the total cost based on the item price and quantity.
    Args:
        item_price (float): The price of the item.
        quantity (int): The quantity of the item.
    Returns:
        float: The total cost.
    """
    total_cost = item_price * quantity
    return total_cost

```

## \*args and \*\*kwargs

- \*args
  - positional arguments
  - dynamic length of arguments
  - treated as a tuple

```py
def my_function(arg1, *args):
    print(f"arg1: {arg1}")
    print(f"args: {args}")

my_function(1, 2, 3, 4, 5)

# arg1: 1
# args: (2, 3, 4, 5)
```

## Study

- data types, variables, operators
- conditional & flow control
- string, list, dict manipulation
- python function and modules
- OOP in python
- Regex & exception handling
- multi threading & python cgi
  - thread safety
  - thread safe functions
