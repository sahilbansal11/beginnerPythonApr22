n = int(input())

# loop over n times, say n = 5
# r = 1, 2, 3, 4, 5
for r in range(1, n + 1):
    # loop over (n - r + 1) times
    for c in range(n - r + 1):
        print('*', end='')
    print()


