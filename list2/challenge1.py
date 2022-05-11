"""
Consider the following program that allows a user
to print the age of the Nth oldest known person
to have ever lived. Note: The ages are in a list sorted from oldest to youngest.

1. Modify the program to print the correct
ordinal number ("1st", "2nd", "3rd", "4th", "5th")
instead of "1th", "2th", "3th", "4th", "5th".
2. For the oldest person, remove the ordinal
number (1st) from the print statement to say,
"The oldest person lived 122 years".

Reminder: List indices begin at 0, not 1,
thus the print statement uses oldest_people[nth_person-1],
to access the nth_person element (element 1 at index 0, element 2 at index 1, etc.).
"""

oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

n = int(input('Enter N (1-5): '))

if n == 1:
    print(f"The oldest person lived {oldest_people[n-1]} years.")
elif n == 2:
    print(f"The 2nd oldest person lived {oldest_people[n-1]} years.")
elif n == 3:
    print(f"The 3rd oldest person lived {oldest_people[n-1]} years.")
elif n == 4:
    print(f"The 4th oldest person lived {oldest_people[n-1]} years.")
elif n == 5:
    print(f"The 5th oldest person lived {oldest_people[n-1]} years.")
else:
    print('Provide a valid value of n')




"""
f-strings introduction

print("The value of n is:", n)
print("The value of n is: " + str(n))
# f-strings
print(f"The value of n is: {n}")
"""
