f = open(r"27b.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    current = [a + b for a in s for b in x]
    d = {y % 10: y for y in sorted(current)}
    s = d.values()
print(max(x for x in s if x % 10 == 8))
# 13608 | 40724928