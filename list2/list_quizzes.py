print('Quiz 1:')
user_values = [2, 5, 9]
user_values[2] = user_values[2] + 1

print(user_values)

print('========')
print('Quiz: 2')
user_values = [3, 5, 9]
user_values[1] = user_values[1] + 1
user_values[2] = user_values[2] + 2

print(user_values)

print('========')
print('Quiz: 3')
user_values = [1, 6, 8]
user_values[1] = user_values[0]

print(user_values)

print('========')
print('Quiz: 4')
user_values = [3, 6, 7]
user_values[1] = user_values[2]
user_values[2] = user_values[0]

print(user_values)

print('========')
print('Quiz: 5')
my_teams = ['Raptors', 'Heat', 'Nets']
your_teams = my_teams
my_teams[1] = 'Lakers'
print('My teams are:', my_teams)
print('Your teams are:', your_teams)
