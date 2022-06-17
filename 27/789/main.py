f = open(r"27-B.txt")
n = int(f.readline())
k1 = 0
k = [0]
ans = 0
for i in range(n):
    c = int(f.readline())
    if c == 1:
        k1 += 1
        k.append(0)
        # print(k1)
    else:
        if c % 2 == 0:
            for j in range(k1 - 2, -1, -2):
                ans += k[j]
            k[k1] += 1
print(ans)
# 8 | 97125499