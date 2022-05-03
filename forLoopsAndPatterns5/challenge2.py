# print all odd integers from 1 to n

n = int(input())

# prints all numbers from 1 to n
for i in range(1, n + 1):
    print(i, end=' ')

print()

# we can increment by 2 now
for i in range(1, n + 1, 2):
    print(i, end=' ')

