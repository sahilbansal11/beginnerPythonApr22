
"""
print('Meow')
print('Meow')
print('Meow')
print('Meow')
print('Meow')
"""

# DRY principle
# DO not repeat yourself


"""
print('start')

counter = 0
if counter != 3: # True, 0 != 3
	print("Meow")
	counter = counter + 2 # executed

print(counter) # 1
print('end')
"""


# print('start')
# initialisation
counter = 0 # -> 2 -> 4 -> 6 -> 8

# while loop syntax
while counter < 3: # loop condition, stops when counter is equal to 3
	# print('counter', counter)
	print('Meow') # work
	counter = counter + 2

# print('end')
