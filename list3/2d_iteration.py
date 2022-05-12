# find the total run made by Sachin in all 3 formats

scores = [
    [75, 100, 82, 76],
    [85, 98, 89, 99],
    [75, 82, 85, 5]
]

print(scores)

total_runs1 = 0
for runs in scores[0]:
    print(runs)
    total_runs1 += runs

print(f'Total runs in row 0: {total_runs1}')

total_runs2 = 0
for runs in scores[1]:
    print(runs)
    total_runs2 += runs

print(f'Total runs in row 1: {total_runs2}')

total_runs3 = 0
for runs in scores[2]:
    print(runs)
    total_runs3 += runs

print(f'Total runs in row 2: {total_runs3}')
