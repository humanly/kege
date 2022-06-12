f = open(r"27b.txt")
n = int(f.readline())
k7, nk7 = 0, 0
cnt = 0
for i in range(n):
    c = int(f.readline())
    if c % 7 == 0:
        cnt += (k7 + nk7)
        k7 += 1
    else:
        cnt += k7
        nk7 += 1
print(cnt)