f = open(r"27-B.txt")
n = int(f.readline())
s_max = 0
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    s_max += max(x)
    curr = [a + b for a in s for b in x]
    d = {y % 10: y for y in reversed(sorted(curr))}
    s = list(d.values())
print(min(x for x in s if x % 10 == s_max % 10))
# 64573 | 189977078