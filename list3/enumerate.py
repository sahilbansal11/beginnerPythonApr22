l = [5, 6, 2, 4]

# x, y = (1, 2)
# print(x)
# print(y)

max_number = l[0]
index_max = 0

for index, number in enumerate(l):
    print(f'index: {index}, number: {number}')
    if number > max_number:
        max_number = number
        index_max = index

print(f'Max number is: {max_number}, max_index is: {index_max}')
