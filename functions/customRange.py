
# default argument
def my_range(end, start = 3):
    print('start', start)
    print('end', end)

    while start < end:
        print(start, end=' ')
        start += 1

# my_range(1, 10)

my_range(10)  # default start = ?
print()
my_range(5)
print()

my_range(1, 10)

print()

my_range(start=1, end=10)
# keyword arguments, more explained in next class
