s = open(r"24.txt").readline()
curr = ''
maxs = ''
for i in range(1, len(s)):
    if (s[i] == 'B' or s[i] == 'C') and s[i - 1] == 'A':
        if s[i] == 'B':
            curr += 'AB'
        else:
            curr += 'AC'
    elif s[i] == 'A':
        continue
    else:
        if len(curr) > len(maxs):
            maxs = curr
        curr = ''
print(len(maxs)//2, maxs)