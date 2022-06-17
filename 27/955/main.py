f = open(r"27b.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    curr = [a + b for a in x for b in s]
    d = {y % 256: y for y in reversed(sorted(curr))}
    s = d.values()
print(min(x for x in s if x % 256 == 31))
# 6687 | 20191263