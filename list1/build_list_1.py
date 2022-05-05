num_matches = int(input('How many matches? '))

idx = 0

# runs = []
runs = list()  # BOTH these ways create an empty list

while idx < num_matches:
    print('idx is', idx, 'and matches is: ', num_matches)
    x = int(input('Please enter the score: '))
    runs.append(x)
    print('The current runs list is:', runs)
    # get the next match data
    idx += 1

print(type(runs))
