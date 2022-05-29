N = int(input())

"""
r
0: 1 2 3 4 5 -> as it is 
1: 6 7 8 9 10 -> reverse order 
2: 11 12 13 14 15 -> as it is
3: 16 17 18 19 20 -> reverse order
4: 21 22 23 24 25 -> as it is


Output: 
1 2 3 4 5 10 9 8 7 6 11 12 13 14 15 20 19 18 17 16 21 22 23 24 25
"""

m = []
for i in range(N):
    l = list(map(int, input().split()))
    m.append(l)

for r in range(N):
    if r % 2 == 0:
        # even row index => left to right
        for c in range(N):
            print(m[r][c], end=' ')
    else:
        # odd row index => right to left
        for c in range(N - 1, -1, -1):
            print(m[r][c], end=' ')

"""
# even index
for c in range(N):
    print(m[0][c], end=' ')

# odd index => reverse
for c in range(N - 1, -1, -1):
    print(m[1][c], end=' ')

# even index
for c in range(N):
    print(m[2][c], end=' ')
    
# odd index => reverse 
for c in range(N - 1, -1, -1):
    print(m[3][c], end=' ')
    
# even index
for c in range(N):
    print(m[4][c], end=' ')

"""

