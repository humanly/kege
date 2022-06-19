f = open(r"27b.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    curr = [a + b for a in s for b in x]
    d = {y % 103: y for y in sorted(curr)}
    s = d.values()
print(max(x for x in s if x % 103 != 0))
# 720367 | 7871426276