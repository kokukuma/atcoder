N = int(raw_input())
res = []
base = N
x = 1
if base == 0:
    print(0)
else:
    while True:
        if base == 0:
            break
        if base % (2 ** x) != 0:
            res.append(1)
            base -= (-2) ** (x-1)
        else:
            res.append(0)
        x += 1
    print(''.join([str(i) for i in reversed(res)]))

