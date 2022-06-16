f = open(r"27b.txt")
n = int(f.readline())
# перебор для A | 18
# a = []
# k = 0
# for i in range(n):
#     a += [int(f.readline())]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if abs(a[i] - a[j]) % 13 == 0 and (a[i] * a[j]) % 2 == 0:
#             k += 1
# print(k)
# ОДИНАКОВЫЙ ОСТАТКИ!
ost = [[0, 0] for i in range(13)]
k = 0
for i in range(n):
    c = int(f.readline())
    if c % 2 == 0:
        k += ost[c % 13][0]
        k += ost[c % 13][1]
    else:
        k += ost[c % 13][0]
    ost[c % 13][c % 2] += 1
    # print(c)
    # print(*ost)
    # input()
print(k)
# 18 | 1821568