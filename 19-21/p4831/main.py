def f(s, p, c, m):
    if s >= 140: return c % 2 == m % 2
    if c == m: return 0
    h = []
    if p != '+1':
        h += [f(s + 1, '+1', c + 1, m)]
    if p != '+2':
        h += [f(s + 2, '+2', c + 1, m)]
    if p != '*3':
        h += [f(s * 3, '*3', c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 140):
    for c in range(1, 15):
        if f(s, '', 0, c) == 1:
            print(s, c)
            break
# 46 16|45 15