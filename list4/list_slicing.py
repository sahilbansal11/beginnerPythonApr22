
a = [1, 9, 2, 8, 4, 3, 7]

b = a[0:4:1]  # start = 0, end = 4, inc = 1

c = a[0:4]  # start = 0, end = 4, default inc = 1

d = a[:4]  # default start = 0, end = 4, default inc = 1

e = a[:]  # default start = 0, default end = len(a), default inc = 1

f = a[:(len(a) - 1)]
g = a[:(len(a))]

print(f)
print(g)
