f = open(r"27-B.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    current = []
    current += [a + x[0] + x[1] for a in s]
    current += [a + x[1] + x[2] for a in s]
    current += [a + x[0] + x[2] for a in s]
    d = {y % 4: y for y in sorted(current)}
    s = d.values()
print(max(x for x in s if x % 4 == 0))
# 18380 | 58701760