n, x = map(int, raw_input().split())
a = map(int, raw_input().split())

if sum(a) < x:
    print(n-1)
else:
    t = 0
    s = 0
    for i in sorted(a):
        s += i
        if s <= x:
            t += 1
            continue
        else:
            break
    print(t)
