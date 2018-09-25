N = int(raw_input())
data = []
for i in range(N):
    data.append(map(int, raw_input().split()))

for d in data:
    if d[0] < d[1] + d[2]:
        print("No")
        exit(0)
    elif d[0] > d[1] + d[2]:
        even0 = d[0] % 2 == 0
        even12 = (d[1] + d[2]) % 2 == 0
        if even0 ^ even12:
            print("No")
            exit(0)
print("Yes")

