import math
a, b = map(int, raw_input().split())
t = int("%d%d" % (a,b))
s = math.sqrt(t)

if s % int(s) == 0:
    print("Yes")
else:
    print("No")
