f = open(r"27-A.txt")
n = int(f.readline())
s = [0]
# for i in range(n):
#     x = [not(int(i) % 2) for i in f.readline().split()]
#     a = [a + b for a in s for b in x]
#     min_delta = 10**20
#     c = [0, 0]
#     for i in range(1, len(a)):
#         if abs(a[i] - a[i - 1]) < min_delta:
#             min_delta = abs(a[i] - a[i - 1])
#             c = [a[i], a[i - 1]]
#     s = c
