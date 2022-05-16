"""
print('Hello')
print('World')

print('How')
print('is')
print('everyone')
"""

"""
print('Hello', 'World', sep='+-%$')

# default separator is space
print('How', 'is', 'everyone', sep=' ')
"""

print('Hello', end='\n') # special character '\n' for the newline
print('World', end='\n') # default is also '\n'

print('How', end=' ') # changed the end as per your need
print('is', end=' ')
print('everyone', end='+++wwfss') # specific to one print statement

print() # new line, end = '\n'

# we can provide both sep and end
print('Hello', 'world', sep='+', end='-') # hello+world-
