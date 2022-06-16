def f(a, b, c, m):
    if a + b >= 59: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a + 2, b, c + 1, m), f(a, b + 2, c + 1, m), f(a * 2, b, c + 1, m), f(a, b * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for b in range(1, 53 + 1):
    for m in range(1, 10):
        if f(5, b, 0, m) == 1:
            print(b, m)
            break


# 14 13 22|23