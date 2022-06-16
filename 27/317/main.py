f = open(r"27-B.txt")
n = int(f.readline())
# перебор для А | 7
# a = []
# for i in range(n):
#     a += [int(f.readline())]
# k = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] + a[j] <= 34 and a[i] > a[j]:
#             k += 1
# print(k)
m = [0 for i in range(34)]
k = 0
for i in range(n):
    c = int(f.readline())
    if c < 34:
        for j in range(c + 1, 35 - c):
            k += m[j]
        m[c] += 1
# print(*m)
print(k)
# 7|1271618