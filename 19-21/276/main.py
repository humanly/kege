def f(s, c, m):
    if s >= 74: return c % 2 == m % 2
    if c == m: return 0
    h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m), f(s * 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 73 + 1):
    for m in range(1, 10):
        if f(s, 0, m) == 1:
            print(s, m)
            break


# 24 8|22|23 21