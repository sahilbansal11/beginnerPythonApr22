
n = int(input())

A = []
for i in range(n):
    x = int(input())
    A.append(x)

print(A)

B = int(input())

# add B to all the element in the list A

# let's update the existing list

# update the existing
# A[0] = A[0] + B
# A[1] = A[1] + B
# A[2] = A[2] + B
# print(A)

for idx in range(n):
    A[idx] = A[idx] + B

print(A)

