"""
Write a code that takes a number as input and prints all the digits of that number
Input: 9145
"""

n = int(input())

print('Start')

count_of_digits = 0
sum = 0
while n > 0:
    # digit
    rem = n % 10
    print(rem)
    # increase the counter
    count_of_digits += 1
    # add the digit to the sum
    sum += rem
    n = n // 10

print('Done')
print('No of digits are:', count_of_digits)
print('Sum of digits is:', sum)
