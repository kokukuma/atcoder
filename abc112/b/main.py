N, T = map(int, raw_input().split())

data = []
for i in range(N):
    c, t = map(int, raw_input().split())
    if t <= T:
        data.append(c)

if len(data) == 0:
    print("TLE")
else:
    data = sorted(data)
    print(data[0])
