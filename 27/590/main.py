f = open(r"27-B.txt")
n = int(f.readline())
# перебор для А | 99
# a = []
# k = 0
# for i in range(n):
#     a += [int(f.readline())]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if (a[i] + a[j]) > 50 and a[j] > a[i]:
#             k += 1
# print(k)
a = [0 for i in range(100 + 1)]
k = 0
for i in range(n):
    c = int(f.readline())
    for j in range(max(51 - c, 1), c): #(!) <- max(50 - c, 1) + 1
        k += a[j]
    a[c] += 1
print(k)
# 99 | 16633163