# default argument

def print_date(day, month, year, style=0):
    if style == 0:  # American
        print(month, '/', day, '/', year)
    elif style == 1:  # European
        print(day, '/', month, '/', year)
    else:
        print('Invalid Style')

print_date(30, 5, 2022)
# print_date(5, 30, 2022)

# print_date("30th", "May", "2022")

# print_date(30, 5, 2022, 1)




