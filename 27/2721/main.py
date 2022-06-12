f = open(r"27a.txt")
n = int(f.readline())
k65, k5, k13 = 0, 0, 0
cnt = 0
for i in range(n):
    c = int(f.readline())
    if c % 65 == 0:
        cnt += i
        k65 += 1
    elif c % 5 == 0:
        cnt += k13 + k65
        k5 += 1
    elif c % 13 == 0:
        cnt += k5 + k65
        k13 += 1
    else:
        cnt += k65
print(cnt)