
# r = int(input('Give the no. of rows: '))
r, c = tuple(map(int, input().split()))
print('No of rows: ', r)
print('No of cols: ', c)

# take r lists as input from the user

final_list = []

for i in range(r):
    current_row = list(map(int, input().split()))
    # actual_int_row = []
    # for ele in current_row:
    #     actual_int_row.append(int(ele))
    # print(actual_int_row)
    # print(current_row)
    final_list.append(current_row)
    # print(final_list)

print(final_list)


