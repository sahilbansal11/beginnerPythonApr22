N = int(input())


for i in range(1, N+1):
    for j in range(N+1-i):
        if j > 0:
            # skip printing for the 1st iteration,
            # print for all the remaining
            print(' ', end='')
        for k in range(j, N):
            print('*', end='')
    print()
