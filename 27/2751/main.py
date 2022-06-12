f = open(r"27b.txt")
n = int(f.readline())
queue = [int(f.readline()) for i in range(4)]
k = [0, 0]
k13 = [0, 0]
cnt = 0
for i in range(n - 4):
    c = int(f.readline())
    if c % 13 == 0:
        cnt += k[not(c % 2)]
    else:
        cnt += k13[not(c % 2)]
    queue.append(c)
    if queue[0] % 13 == 0:
        k13[queue[0] % 2] += 1
    k[queue[0] % 2] += 1
    queue.pop(0)
print(cnt)