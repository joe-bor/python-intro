# iterate over multiple lists until end of the shortest iterable
# zip(iterable1, iterable2)
    # yields tuples of (elem1[index], elem2[index])
    # returns a generator -> probably best not to store in variable because of this
    
names = ["Bob", "Alice", "Eve", "Joe"]
scores = [42, 97, 68]

print(type(zip(names, scores)))

for name, score in zip(names, scores):
    print(f'{name} had a score of {score}')
    

# Create a dict using 2 lists
score_dict = dict(zip(names, scores))
print(score_dict)