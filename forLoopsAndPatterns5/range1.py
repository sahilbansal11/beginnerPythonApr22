print(range(6))  # this is not helpful

print(list(range(6)))  # converting this to a list
# we will talk about list in the next classes

print(list(range(2, 8)))
# [2, 3, 4, 5, 6, 7]

print(list(range(-1, 10, 2)))  # values < 10 are included
# [-1, 1, 3, 5, 7, 9]

print(list(range(10, 0, -2)))  # values > 0 are included
# [10, 8, 6, 4, 2]

print(list(range(10, 12, -2)))  # values > 12 are included
# 10 itself is not greater than 12
# does not include anything

# []

print(list(range(5, 1)))  # start = 5, end = 1, inc = 1
# values < end, 5 itself is not less than end
# []
