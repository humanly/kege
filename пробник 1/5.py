for i in range(10, 1001):
    n = i
    n = bin(n)[2:]
    q = ''
    for j in range(1, len(n)):
        if n[j] == '1':
            q = n[j:]
    ans = 0
    if len(q) == 0:
        ans = 0
    else:
        ans = int(n, 2)
    