f = open(r"27b.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    curr = [a + b for a in s for b in x]
    d = {y % 3: y for y in reversed(sorted(curr))}
    s = d.values()
print(min(x for x in s if x % 3 != 0))
# 67303 | 200157496