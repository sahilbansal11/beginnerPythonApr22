# Challenge 8: Read a num and
# check last digit is 4.

x = float(input())

if x % 10 == 4:
	print(True)
else:
	print(False)

print('Done')
print('Last digit is:', x % 10)
