names = ["Nina", "Max", "Rose", "Jimmy"]

# BEFORE:
my_list = [] # empty list
for name in names:
    my_list.append(len(name))
    
print(my_list)

#AFTER: w/ list comprehension
# print([len(name) for name in names])


print([name for name in names if len(name) % 2 == 0])


#
my_nums =  [1, 2, 3]
times_two = [num*2 for num in my_nums]
print(times_two)

my_names = ['Joe', 'Ethan', 'Mimi']
split_names = ", ".join([ "hello " + name for name in my_names])
print(split_names)