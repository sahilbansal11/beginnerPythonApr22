# print a^b

a = int(input())
b = int(input())

ans = 1
for i in range(b):  # range(1, b + 1) also works
    ans *= a
    print('ans now is: ', ans)

print('final ans is: ', ans)
