# coordinates of a location input from the user
"""
x, y = input().split()
print(x, y)
print(type(x), type(y))

x = int(x)
print(type(x))

y = int(y)
print(type(y))

# print x^2, y^2
print(x*x, y*y)
"""
x = input().split()
print('List of strings:', x)

int_coordinates = list(map(int, x))
print('List of integers:', int_coordinates)

# input_list = list(map(int, input().split()))
# print(input_list)

# get the tuple as input
input_tuple = tuple(int_coordinates)
print('Tuple of coordinates:', input_tuple)

# also do the reverse conversion tuple to list

tuple_from_list = list(input_tuple)
print('Tuple from the list:', tuple_from_list)




