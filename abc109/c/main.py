from fractions import gcd
n, s = map(int, raw_input().split())
xs = [ int(i) for i in raw_input().split()]
diff = [ abs(x-s) for x in xs]
print(reduce(gcd, diff))
