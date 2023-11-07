'''
practice
'''
# Let’s practice our comprehensions. Create a list of only odd numbers between 0 and 100 using a list comprehension.
odd_nums_list = [num for num in range(0, 100) if num % 2 != 0]
print(odd_nums_list)

#Then, use a comprehension to create a dictionary where the keys are the odd numbers from your list, and the values are random integers between 0 and 100 (hint: try random.randint(min, max)).
import random
from pprint import pprint
my_dict =  {num:random.randint(0, 100) for num in odd_nums_list }
pprint(my_dict)

# Finally, use a comprehension to create a set of every unique value from the above dictionary.

my_set = {value for value in my_dict.values()}
print(type(my_set), my_set)