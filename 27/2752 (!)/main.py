f = open(r"27a.txt")
n = int(f.readline())
cnt = 0
# перебор
a = [int(f.readline()) for x in range(n)]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if (j - i) >= 6 and (a[j] * a[i]) % 10 == 3:
            cnt += 1
print(cnt)