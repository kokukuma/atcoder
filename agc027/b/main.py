N, X = map(int, raw_input().split())
x = map(int, raw_input().split())

print(N, X, x)

en = X * (N + 1)
print(en)
before = None
x.append(0)
for i, v in enumerate(sorted(x, reverse=True)):
    if i == 0:
        en += ((i + 1) ** 2) * v
    else:
        en += ((i + 1) ** 2) * (before - v)
    before = v

    print(en)


