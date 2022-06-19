f = open(r"27_B.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    curr = [a + b for a in s for b in x]
    d = {y % 101: y for y in sorted(curr)}
    s = d.values()
print(max(x for x in s if x % 101 != 0))
# 694390 | 7567616720