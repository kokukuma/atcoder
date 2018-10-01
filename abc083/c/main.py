x, y = map(int, raw_input().split())
i = 1
f = x
while True:
    if f * 2 > y:
        break
    f *= 2
    i += 1
print(i)
