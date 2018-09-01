s = raw_input()
k = raw_input()

f = True
for i, n in enumerate(s):
    if n != "1":
        f = False
        print(n)
        break
    if i+1 == int(k) and f:
        print(1)
        break

