f = open(r"27b.txt")
n = int(f.readline())
max_k23 = [0, 0]
max_oth = [0, 0]
max_sum = 0
for i in range(n):
    c = int(f.readline())
    if c % 23 == 0:
        max_sum = max(max_sum, c + max_oth[c % 2], c + max_k23[c % 2])
        max_k23[c % 2] = max(max_k23[c % 2], c)
    else:
        max_sum = max(max_sum, c + max_k23[c % 2])
        max_oth[c % 2] = max(max_oth[c % 2], c)
print(max_sum)