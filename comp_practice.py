'''
practice
'''
# Let’s practice our comprehensions. Create a list of only odd numbers between 0 and 100 using a list comprehension.
odd_nums_list = [num for num in range(0, 100) if num % 2 != 0]
# print(odd_nums_list)

#Then, use a comprehension to create a dictionary where the keys are the odd numbers from your list, and the values are random integers between 0 and 100 (hint: try random.randint(min, max)).
import random
from pprint import pprint
my_dict =  {num:random.randint(0, 100) for num in odd_nums_list }
# pprint(my_dict)

# Finally, use a comprehension to create a set of every unique value from the above dictionary.

my_set = {value for value in my_dict.values()}
# print(type(my_set), my_set)


'''
You know how to create a list of even or odd numbers with a list comprehension. Make a list of numbers between 0 and 100, then try making a list of even numbers between 30 and 70, by taking a slice from the first list. Then, make a new list in the reverse order.
'''

my_list = [num for num in range(0,100)]
# print(my_list)

thirty_to_seventy_list = my_list[30:70]
# print(thirty_to_seventy_list)

new_list = thirty_to_seventy_list[::-1]
# print(new_list)

'''
Make a list of all the names you can think of, called “names”. Make a second list of numbers, called “scores”, using a list comprehension and random.randint(min, max) as before. Use the first list in your comprehension to make it the same length. Then, use zip() to output a simple scoreboard of one score per name.
'''

names = ['Joe', 'Ethan', 'Mimi']
scores = [random.randint(0, 10) for name in names]

for name, score in zip(names, scores):
    print(f"{name} got {score}")