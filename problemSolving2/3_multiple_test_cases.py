# You need to take T nums as input from the user
# and just print the number back to the screen

# Input:
# 3
# 123
# 466
# 17

# Output:
# 123
# 466
# 17

T = int(input())

def sum_of_digits(x):
	# print sum of digits
	s = 0
	while x > 0:
		s += (x % 10)
		x = x // 10
	return s

"""
i = 1
while i <= T:
	x = int(input())
	
	# any logic perform with this x
	s = sum_of_digits(x)
	print(s)

	i += 1
"""

for i in range(T): # i = 0, 1, ... T - 1
	x = int(input())

	s = sum_of_digits(x)
	print(s)

