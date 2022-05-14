T = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', 'O', 'X']
]

# print(T[0][0], T[0][1], T[0][2])
# print(T[1][0], T[1][1], T[1][2])
# print(T[2][0], T[2][1], T[2][2])

r = len(T)
c = len(T[0])

for i in range(r):
    for j in range(c):
        print(T[i][j], end=' ')
    # print a new line after the row is done
    print()
