def f(a, b, c, m):
    if a + b >= 80: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a + b, b, c + 1, m), f(a, a + b, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else any(h)


for b in range(1, 60):
    for m in range(1, 10):
        if f(20, b, 0, m) == 1:
            print(b, m)
            break


# 30 14|29 10