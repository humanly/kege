f = open(r"27b.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    curr = []
    curr += [a + x[0] + x[1] for a in s]
    curr += [a + x[0] + x[2] for a in s]
    curr += [a + x[2] + x[1] for a in s]
    d = {y % 5: y for y in sorted(curr)}
    s = d.values()
print(max(x for x in s if x % 5 != 0))
# 25034 | 76468978