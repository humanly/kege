f = open(r"27a.txt")
n = int(f.readline())
# a = [int(f.readline()) for x in range(n)]
# k = 0
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if (j - i) <= 7 and (a[i] + a[j]) % 8 != 0:
#             k += 1
# print(k)
queue = [int(f.readline()) for x in range(7)]
kr = [0 for i in range(8)]
cnt = 0
for i in queue:
    kr[i % 8] += 1
for i in range(1, 4):
    cnt += sum(kr) - kr[8 - i] - kr[i]
print(kr, cnt)
for i in range(n - 7):
    c = int(f.readline())
