
n = int(input())

for r in range(1, n):

    # print (n - r + 1) *s
    for c in range(n - r + 1):
        print('*', end='')

    # print 2*(r - 1) spaces
    for c in range(2*(r - 1)):
        print(' ', end='')

    # print (n - r + 1) *s
    for c in range(n - r + 1):
        print('*', end='')

    print()

# code for the HW (challenge 7)
for r in range(1, n + 1):
    for c in range(r):
        print('*', end='')

    for c in range(2*(n - r)):
        print(' ', end='')

    for c in range(r):
        print('*', end='')
    print()
