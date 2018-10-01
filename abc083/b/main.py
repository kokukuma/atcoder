n, a, b = map(int, raw_input().split())
l = []
for i in range(1, n+1):
    s = sum([int(j) for j in ("%d" % i)])
    if a <= s <= b:
        l.append(i)
print(sum(l))
