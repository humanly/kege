f = open(r"27-B.txt")
n = int(f.readline())
# перебор для А | 72
# a = []
# k = 0
# for i in range(n):
#     a += [int(f.readline())]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if (a[i] + a[j]) % 2 == 0 and 0 in a[i: j + 1] and a[i] > 0 and a[j] > 0:
#             k += 1
#             print(a[i], a[j])
# print(k)
k2 = [0, 0]
k = 0
nakop = [0, 0]
for i in range(n):
    c = int(f.readline())
    if c > 0:
        k += k2[c % 2]
        nakop[c % 2] += 1
    else:
        k2[0] += nakop[0]
        k2[1] += nakop[1]
        nakop = [0, 0]
print(k)
# 51 | 24019058