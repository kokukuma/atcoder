H, W = map(int, raw_input().split())
# print(H, W)

slist = []
slist.append(["." for j in range(W+2)] )
for i in range(H):
    l = [j for j in raw_input()]
    l.insert(0, ".")
    l.append(".")
    slist.append(l)
slist.append(["." for j in range(W+2)])
# for s in slist:
#     print(s)

for i in range(1, H):
    for j in range(1, W):
        if slist[i][j] == "#":
            if slist[i+1][j] == "." and slist[i][j+1] == "." and \
               slist[i-1][j] == "." and slist[i][j-1] == ".":
                print("No")
                exit(0)
print("Yes")
