f = open(r"27-B.txt")
n = int(f.readline())
# перебор для А | 77
# a = []
# k = 0
# for i in range(n):
#     a += [int(f.readline())]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if (a[i] + a[j]) % 2 != 0 and a[j] > min(x for x in a[0:j + 1] if x % 2 != a[j] % 2):
#             k += 1
# print(k)
min_k2 = [10**20, 10**20]
k2 = [0, 0]
k = 0
for i in range(n):
    c = int(f.readline())
    if c > min_k2[not(c % 2)]:
        k += k2[not(c % 2)]
    min_k2[c % 2] = min(min_k2[c % 2], c)
    k2[c % 2] += 1
print(k)
# 77 | 24970659