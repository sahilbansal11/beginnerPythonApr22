scores = [
    [1, 2, 3],
    [5, 3],
    [6, 3]
]

num_rows = len(scores)

total_runs = 0
for r in range(num_rows):
    # size of elements in the row r
    num_cols = len(scores[r])

    for c in range(num_cols):
        # print(r, c)
        # print(scores[r][c])
        print(f'{r},{c}: {scores[r][c]}')
        total_runs += scores[r][c]

print(f'Total runs: {total_runs}')
