A = int(input())

counter = 1
final_result = 0
while counter <= A:
    if counter % 2 == 0:
        # if it's even, update the final_result
        final_result += counter
    counter += 1

print(final_result)
