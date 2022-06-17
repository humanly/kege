f = open(r"27-A.txt")
n = int(f.readline())
# перебор для А | 19
# a = []
# k = 0
# for i in range(n):
#     a += [int(f.readline())]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         for k in range(j + 1, len(a)):
#             curr = [a[i], a[j], a[k]]
#             # curr.sort()
#             if curr[0] + curr[1] == curr[2]:
#                 k += 1
# print(k)
k = 0
q = [int(f.readline()) for i in range(2)]
s = set()
s.add(q[0] + q[1])
for i in range(n - 2):
    c = int(f.readline())
    if c in s:
        k += 1
    q = [c + x for x in sorted(s)]
    s = set(sorted(s) + q)
    # print(*s)
    # input()
print(k)