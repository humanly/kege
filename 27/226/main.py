f = open("27b.txt")
n = int(f.readline())
# перебор для А | 15
# a = []
# for i in range(n):
#     a += [int(f.readline())]
# k = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if (a[i] + a[j]) % 2 == 0 and (a[i] + a[j]) % 5 == 0:
#             k += 1
# print(k)
ost = [[0, 0] for i in range(5)]
k = 0
for i in range(n):
    c = int(f.readline())
    k += ost[5 - (c % 5)][c % 2] if c % 5 != 0 else ost[0][c % 2]
    ost[c % 5][c % 2] += 1
print(k)
# 15 | 5001021