# say we want to break at 50

for i in range(100):
    print(i, end=' ')
    if i == 50:
        break


print()

# we can also break the loop directly

for i in range(100):
    print(i)
    break

