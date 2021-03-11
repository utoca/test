with open('input.txt','r') as f:
    S = [s.strip() for s in f.readlines()]
    #s = f.readline()
D = []
for s in S:
    s = s.split(':')
    if len(s) == 2:
        D.append([int(s[0]),s[1]])
    else:
        m = int(s[0])


D.sort(key=lambda x:x[0])
ans = ''
for d in D:
    if m%d[0] == 0:
        ans = ans + d[1]
if len(ans) == 0:
    print(m)
else:
    print(ans)
