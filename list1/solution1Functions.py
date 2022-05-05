# In the assignment, no need to take any input
# Only write the function

# A is a list
# B is an integer
def solve(A, B):
    n = len(A)

    for i in range(n):
        A[i] = A[i] + B

    return A

res = solve([9, 1, 2, 5, 6], 4)
print(res)
