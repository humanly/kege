f = open(r"27b.txt")
n = int(f.readline())
max_k2, max_nk2 = 0, 0
max_sum = 0
for i in range(n):
    c = int(f.readline())
    if c % 2 == 0:
        max_sum = max(max_sum, c + max_nk2)
        max_k2 = max(max_k2, c)
    else:
        max_sum = max(max_sum, c + max_k2)
        max_nk2 = max(max_nk2, c)
print(max_sum)