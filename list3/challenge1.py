"""
Given an array, find the maximum value in the array.

l = [1, 2, 5, 3, 2, 5, 6, 4]
"""

l = [1, 2, 5, 3, 2, 5, 6, 4]

max_number = l[0]

for index in range(1, len(l)):
    number = l[index]

    if number > max_number:
        max_number = number

print(f"The maximum number is {max_number}")


