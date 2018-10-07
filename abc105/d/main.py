N, M = map(int, raw_input().split())

a = []
x = 1
while x * x <= M:
    if M % x == 0:
        a.append(x)
        a.append(M/x)
    x += 1

res = 0
for i in a:
    if M / i >= N:
        res = max(res, i)
print(res)
