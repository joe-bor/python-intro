names = ["Nina", "Max", "Rose", "Jimmy"]

# BEFORE:
my_list = [] # empty list
for name in names:
    my_list.append(len(name))
    
print(my_list)

#AFTER: w/ list comprehension
# print([len(name) for name in names])


print([name for name in names if len(name) % 2 == 0])

# ---

my_nums =  [1, 2, 3]
times_two = [num*2 for num in my_nums]
print(times_two)

my_names = ['Joe', 'Ethan', 'Mimi']
split_names = ", ".join([ "hello " + name for name in my_names])
print(split_names)

# get the sum of chars in the my_names list
# sum, min max -> accepts list of numbers
chars_sum = sum([len(name) for name in my_names])
print(chars_sum)



# --- Dict comprehension ---
print("---\nDict Comprehension:\n---")

# similar to list comprehensions
# except they take key and value separated by :
squares = {num:num for num in range(4)}
print(squares)

# w/ f-strings -> ie keeping track of scores
scores = {f"player-{num}":0 for num in range(3)}
print(scores)

# combining comprehensions
print("\n combining comprehensions:")

# a list of tuples -> [ ( , ),  (, ), (, ) ]
my_list = [(f'player-{num}', num * 2) for num in range(0, 3)]
print(my_list)
# for key, value in my_list:
#     print(key, value)

# create a dict using dict comprehension using the list created w/ list comprehension
scores = {key:value for (key,value) in my_list}
print(scores)
