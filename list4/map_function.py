
l = [4, 1, 2, 3]
# get the squares of all these elements in a list
l2 = []
for x in l:
    l2.append(x*x)

print(l2)

# using the map function
def square(x):
    return x*x

# l2 = map(square, l) # how to get the list out of it?
# print(l2)

# convert it to a list
l2 = list(map(square, l))
print(l2)

"""
# analogy
l3 = list(range(10, 15))
print(l3)
"""
