# Given a list of integers as input in a single line
# And given a number x in the next line
# Find the index of the element x (1st occurrence of the value x)

"""
Input:

3 4 2 4 5 7 8
5
"""

user_input = input()
# print(user_input)
# print(type(user_input))

numbers = user_input.split()
# print(numbers)
# print(type(numbers)) # list of strings

# do we know how to convert a string to num
# x = '3'
# y = int(x)

final_list = []
for number in numbers:
    final_list.append(int(number))

print(final_list)

# the number x that we want to search for
x = int(input())

idx = 0
for final_number in final_list:
    if final_number == x:
        print('Element found at position', idx)
        break # stop the loop as soon as the element is found

    idx += 1
