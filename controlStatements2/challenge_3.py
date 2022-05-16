# Challenge 3:
# Print all the odd numbers from 1 to N

# N = 10
# 1, 3, 5, 7, 9


n = int(input())


# LOGIC 1
counter = 1

while counter <= n:
    if counter % 2 == 1: # odd number then only print
        print(counter, end = ' ') # only when counter is odd
    # for even number we are not printing
    counter = counter + 1


"""
LOGIC 2
counter = 1
while counter <= n:
    print(counter, end = ' ')
    counter = counter + 2 # because we want to print at gap of 2
"""
