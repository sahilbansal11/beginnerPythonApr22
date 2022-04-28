# Challenge
# Read a number n and print the reverse for it
# by storing it in an integer
# Input: 529
# Output: 925

n = int(input())

# print(n)
reverse_n = 0

while n > 0:
    rem = n % 10
    print(rem)

    # last challenge
    # adding to the end a digit
    reverse_n = (reverse_n * 10) + rem
    n = n//10
    print('reverse till now', reverse_n)

print('n is now zero', n)
print(reverse_n)

# Now can you print the digits
# 5
# 2
# 9

while reverse_n > 0:
    rem = reverse_n % 10
    print(rem)

    reverse_n = reverse_n // 10
