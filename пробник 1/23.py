def f(begin, end):
    if begin == end: return 1
    elif begin > end: return 0
    else: return f(begin + 2, end) + f(begin * 2, end)
print(f(1, 16) * f(16, 52))
