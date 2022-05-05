n = int(input())

for r in range(1, n + 1):
    for c in range(1, n - r + 1):
        print(0, end='')

    for c in range(r, 2*r):
        print(c, end='')

    for c in range(2*(r - 1), r - 1, -1):
        print(c, end='')

    for c in range(1, n - r + 1):
        print(0, end='')

    # if it's the last row, then do no print a new line
    if r < n:
        print()
