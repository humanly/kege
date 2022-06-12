f = open(r"27b.txt")
n = int(f.readline())
k5_nk2, k5_k2, nk2, k2 = 0, 0, 0, 0
cnt = 0
for i in range(n):
    c = int(f.readline())
    if c % 5 == 0:
        if c % 2 == 0:
            cnt += nk2 + k5_nk2
            k5_k2 += 1
        else:
            cnt += k2 + k5_k2
            k5_nk2 += 1
    elif c % 2 == 0:
        cnt += k5_nk2
        k2 += 1
    else:
        cnt += k5_k2
        nk2 += 1
print(cnt)