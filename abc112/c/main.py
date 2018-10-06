N = int(raw_input())
data = []
for i in range(N):
    v = map(int, raw_input().split())
    data.append(v)

cond = []
for x in range(100+1):
    for y in range(100+1):
        h = []
        for d in data:
            if d[2] != 0:
                h.append(d[2] + abs(d[0]-x) + abs(d[1]-y))
        if len(set(h)) == 1:
            cond.append((x, y, h[0]))

if len(cond) == 1:
    print cond[0][0], cond[0][1], cond[0][2]
else:
    for c in cond:
        res = []
        for d in data:
            if d[2] == 0:
                if c[2] - (abs(d[0]-c[0]) + abs(d[1]-c[1])) <= 0:
                    res.append(True)
                else:
                    res.append(False)
        if all(res):
            print c[0], c[1], c[2]
            exit(0)

