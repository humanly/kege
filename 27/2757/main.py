f = open(r"27b.txt")
n = int(f.readline())
queue = [int(f.readline()) for i in range(8)]
k = 0
k23 = 0
cnt = 0
for i in range(n - 8):
    c = int(f.readline())
    if c % 23 == 0:
        cnt += k
    else:
        cnt += k23
    k += 1
    if queue[0] % 23 == 0:
        k23 += 1
    queue.append(c)
    queue.pop(0)
print(cnt)