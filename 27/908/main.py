f = open(r"27b.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    current = [a + b for a in s for b in x]
    d = {y % 16: y for y in reversed(sorted(current))}
    s = d.values()
print(min(x for x in s if x % 16 == 15))
# 6495 | 20191039