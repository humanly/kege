f = open(r"27b.txt")
n = int(f.readline())
min_k31, min_oth = 10**20, 10**20
min_p = 10**20
for i in range(n):
    c = int(f.readline())
    if c % 31 == 0:
        min_p = min(min_p, c * min_oth, c * min_k31)
        min_k31 = min(min_k31, c)
    else:
        min_p = min(min_p, c * min_k31)
        min_oth = min(min_oth, c)
print(min_p)