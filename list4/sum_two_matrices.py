a = [
    [1, 2, 3],
    [3, 4, 5]
]

b = [
    [6, 7, 8],
    [9, 10, 11]
]

res = []

r = len(a)
c = len(a[0])

for i in range(r):
    row = []
    for j in range(c):
        sum = a[i][j] + b[i][j]
        row.append(sum)
        print(sum)
    print(row)
    res.append(row)

print(res)
