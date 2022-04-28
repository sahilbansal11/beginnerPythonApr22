# Challenge
# Read N, and a single digit d
# Add digit d to the back of N

n = int(input())
d = int(input())

# map and split functions we will learn in the later classes
# for now we can use it directly
# n, d = map(int, input().split())

print('n', n)
print('d', d)

print(n*10 + d)

