f = open(r"26.txt")
n = int(f.readline())
a = [[] for i in range(100001)]
for i in range(n):
    x, y = map(int, f.readline().split())
    a[x].append(y)
maxx = [0, 0]
for i in range(n):
    if len(a[i]) >= 2:
        a[i].sort()
        for j in range(1, len(a[i])):
            if abs(a[i][j - 1] - a[i][j]) == 12:
                if maxx[0] != i:
                    maxx[0] = i
                    maxx[1] = a[i][j - 1] + 1
print(*maxx)