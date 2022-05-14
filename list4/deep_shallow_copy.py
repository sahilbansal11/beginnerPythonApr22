# shallow copy
a = [4, 2, 1, 3]

b = a

a[0] = 3

b[2] = 0

print(a)
print(b)

# deep copy

a = [4, 2, 1, 3]

b = a[:]

a[0] = 3

b[2] = 0

print(a)
print(b)
