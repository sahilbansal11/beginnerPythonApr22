# WHY are we not allowed to keep default arguments in
# the starting

# ALL THE DEFAULT ARGUMENTS SHOULD COME AT THE END

def introduce(age = 22, name = 'Sahil'):
    print('Hello, I am', name)
    print('I am', age, 'years old')
    print()


introduce('Rishi')
# introduce(23)
# introduce(25, 'Rishi')

# Does not allow default arguments in the start
"""
def add(n1 = 2, n2):
    return n1 + n2

print(add(3, 5))
"""
