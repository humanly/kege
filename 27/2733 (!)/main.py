f = open(r"27a.txt")
n = int(f.readline())
kr = [[] for i in range(81)]
cnt = 0
for i in range(n):
    c = int(f.readline())
    if c > 50000:
        if c % 80 == 0:
            cnt += len(kr[0])
        else:
            cnt += len(kr[80 - (c % 80)])
    if c % 80 != 0:
        kr[80 - (c % 80)] += [c]
    else:
        kr[0] += [c]
print(cnt)