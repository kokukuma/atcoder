N, M = map(int, raw_input().split())
A = map(int, raw_input().split())

AX = []
s = 0
for a in A:
    s += a
    AX.append(s)

B = {}
B[0] = 1
for i in range(N):
    e = AX[i] % M
    if e not in B:
        B[e] = 1
    else:
        B[e] += 1

res = 0
for _,v in B.items():
    res += v * (v-1) / 2

print(res)


