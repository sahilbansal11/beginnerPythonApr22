print(list(range(-1, 10, 2)))

# what if we want to pick these values one by one
# we can simply use a for loop to iterate one by one

for i in range(-1, 10, 2):
    print(i, end=' ')

# now let us say we want to print their squares
print()  # prints a new line

for i in range(-1, 10, 2):
    print(i * i, end=' ')


# let's say we want to find the sum of these numbers

sum = 0
for i in range(-1, 10, 2):
    sum += i

print()
print('sum of all these numbers', sum)

print()
print('Now using while loop')

i = -1
while i < 10:
    print(i * i, end=' ')
    i += 2
