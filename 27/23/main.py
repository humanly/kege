# Метод частичных сумм
f = open("27b.txt")
n = int(f.readline())
s = [0]
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    current = [a + b for a in x for b in s]
    d = {y % 3: y for y in sorted(current)}
    s = d.values()
print(max(x for x in s if x % 3 != 0))
# 127127|399762080