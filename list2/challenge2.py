"""
Modify short_names by deleting the first element and changing the last element to Joe.

Sample output with input: 'Gertrude Sam Ann Joseph'
['Sam', 'Ann', 'Joe']
"""

short_names = ['Gertrude', 'Sam', 'Ann', 'Joseph']

print('Original list is:')
print(short_names)

n = len(short_names)
# print(short_names[n - 1])
print(short_names[-1])

# short_names[n - 1] = 'Joe'
short_names[-1] = 'Joe'
print('Updating the last element to Joe')
print(short_names)

print('Deleting the first element')
# short_names.remove('Gertrude')
short_names.pop(0)
print(short_names)
