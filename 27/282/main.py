f = open(r"27b.txt")
n = int(f.readline())
# перебор для А | 583263
# a = []
# for i in range(n):
#     a += [int(f.readline())]
# mx = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if abs(i-j) >= 8:
#             mx = max(mx, a[i] * a[j])
# print(mx)
q = [int(f.readline()) for i in range(7)]
mx, mxk = 0, 0
for i in range(n - 7):
    c = int(f.readline())
    mx = max(mx, c * mxk)
    mxk = max(q[0], mxk)
    q.pop(0)
    q.append(c)
print(mx)
# 583263 | 998001