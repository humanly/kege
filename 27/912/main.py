f = open(r"27b.txt")
n = int(f.readline())
minn = 0
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    minn += min(x)
    curr = [a + b for a in s for b in x]
    d = {y % 7: y for y in sorted(curr)}
    s = d.values()
print(max(x for x in s if x % 7 == minn % 7))
# 115110 | 410884352