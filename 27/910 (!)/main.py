f = open(r"27b.txt")
n = int(f.readline())
s = [0]
s_all = 0
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    s_all += sum(x)
    curr = [a + b for a in x for b in s]
    d = {y % 2: y for y in (sorted(curr))}
    s = list(d.values())
print(s_all, s)
