# print all integers from 1 to n

n = int(input())

# this does not print the value N=n
for i in range(1, n):  # starting at 1, ending at n
    print(i, end=' ')

print()


# this will print all values from 1 to n
for i in range(1, n + 1):
    # end = n + 1, because we want n to included
    print(i, end=' ')

