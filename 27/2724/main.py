f = open(r"27b.txt")
n = int(f.readline())
kr = [0 for i in range(132)]
cnt = 0
for i in range(n):
    c = int(f.readline())
    if c % 131 != 0:
        cnt += kr[131 - (c % 131)]
    else:
        cnt += kr[0]
    kr[c % 131] += 1
print(cnt)