f = open(r"27a.txt")
N = int(f.readline())
s = [int(x) for x in f]
ans = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] * s[j] % 6 == 0:
            ans += 1
print(ans)