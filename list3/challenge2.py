"""
Given an array, find the index for maximum value in the array.

l = [1, 2, 5, 3, 2, 6, 5, 4, 6]
"""

l = [5, 6, 2, 4]

max_number = l[0]
index_max = 0

for index in range(1, len(l)):
    number = l[index]

    if number > max_number:
        max_number = number
        index_max = index
print(f"The maximum number is {max_number}")








"""
idx = 0
for number in l:
    if number == max_number:
        print('Element found at position', idx)
        break # stop the loop as soon as the element is found

    idx += 1

# print(f"The index for maximum number is {l.index(max_number)}")
print(f"The index for maximum number is {idx}")
"""
