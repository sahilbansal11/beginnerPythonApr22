# Challenge 4:

# Print all the 10 multiples of 17

'''
multiple = 17
print('Multiple before start of the loop', multiple)

while multiple <= 170: # 17*10
    # this will stop when multiple = 170+17 = 187
    print(multiple, end=' ') # end = space
    multiple = multiple + 17 # shorthand, multiple += 17

# this is the end of the while loop
print()
print('Multiple after end of the loop', multiple)
'''

n = int(input())
counter = 1

# n, 2*n, 3*n, 4*n, ... 10*n
# 1*n, 2*n, 3*n, ... 10*n
while counter <= 10: # stop when counter is 11
    print(counter*n, end=' ')
    counter += 1 # counter = counter + 1 is the same

