f = open(r"27-B.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    current = [a + b for a in s for b in x]
    d = {y % 5: y for y in reversed(sorted(current))}
    s = d.values()
print(min(x for x in s if x % 5 != 0))
# 214 | 334771