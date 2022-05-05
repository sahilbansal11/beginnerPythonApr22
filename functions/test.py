
def f(a, b, c, d = 1, e = 2, f = 3):
    print('d', d)
    print('e', e)
    print('f', f)
    print('something')

# skip d
# pass e
f(1, 2, 3, e = 4)
