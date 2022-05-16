def percentage_grade(m1,m2,m3,m4,m5):
	total = m1 + m2 + m3 + m4 + m5
	per= total / 5

	res = str(int(per))
	res += '\n'
	if per >= 90:
		res += 'A'
	elif per >= 80:
		res += 'B'
	elif per >= 70:
		res += 'C'
	elif per >= 60:
		res += 'D'
	elif per >= 40:
		res += 'E'
	else:
		res += 'F'
	return res

# this code is already present
t=int(input())
while t!=0:
	m1 = float(input())
	m2 = float(input())
	m3 = float(input())
	m4 = float(input())
	m5 = float(input())
	print(percentage_grade(m1,m2,m3,m4,m5))
	t-=1

