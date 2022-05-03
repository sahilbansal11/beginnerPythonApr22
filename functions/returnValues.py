
def add_2_nums(n1, n2):
    print(n1 + n2)


x = add_2_nums(1, 2)
print(x)
print()

# try to return some value now

def add_2_nums_with_return(n1, n2):
    return n1 + n2

y = add_2_nums_with_return(5, 6)
print(y)

if y % 2 == 0:
    print('Result of addition is even')
else:
    print('Result of addition is odd')

