# Challenge 5:
# Given a number print if it is +ve, -ve or zero

x = int(input())

# nested if else
if x > 0:
	print('x is positive')
else:
	if x < 0:
		print('x is negative')
	else:
		print('x is zero')

# if else if
# more readable, easy to understand
if x > 0:
	print('x is positive')
elif x < 0:  # just kind of combined line 9 and 10
	print('x is negative')
else:
	print('x is zero')

