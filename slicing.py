my_string = "0123456789"
#regular indexing
print(my_string[0])

# from start to 7
print(my_string[:7])

# from 2 to end
print(my_string[2:])

# from 3 to 5
print(my_string[3:5])

# start to end
print(my_string[:])

# quick SHALLOW COPY
copy_string = my_string[:]
print(copy_string is my_string) #True

my_list = [1, 2, 3]
copy_list = my_list[:]
print(my_list is copy_list) # False -> shallow copy / same contents / diff pointers

# negative indexing is possible in python
print(my_string[-1])

# STRIDE or STEP -> 3rd argument [start : stop : step]
print(my_string[::2])