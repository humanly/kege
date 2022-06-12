f = open(r"27a.txt")
n = int(f.readline())
# k2, nk2 = [], []
# for i in range(n):
#     c = int(f.readline())
#     if c % 2 == 0:
#         k2.append(c)
#     else:
#         nk2.append(c)
# k = (len(k2) * (len(k2) - 1) // 2) + (len(nk2) * (len(nk2) - 1) // 2)
# print(k)
k2, nk2 = 0, 0
cnt = 0
for i in range(n):
    c = int(f.readline())
    if c % 2 == 0:
        cnt += k2
        k2 += 1
    else:
        cnt += nk2
        nk2 += 1
print(cnt)