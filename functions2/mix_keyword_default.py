def print_date(day=1, month=1, year=2022, style=0):
    if style == 0:  # American
        print(month, '/', day, '/', year)
    elif style == 1:  # European
        print(day, '/', month, '/', year)
    else:
        print('Invalid Style')

print_date(day=30, year=2022)

print_date(day=5, style=1, month=5)
