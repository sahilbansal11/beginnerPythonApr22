# Challenge 5:
# Given N = 3 print
"""
* => 1 star
** => 2 stars
*** => 3 stars

start = 1
end = N + 1
inc = 1

range(1, N + 1)
"""

N = int(input())
# how can I print numbers from 1 to N?

for i in range(1, N + 1):
    # print(i)
    # how can I print i stars?
    for j in range(i):
        print('*', end='')
    # after printing one row, we print a new line
    print()

