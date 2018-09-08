n = int(raw_input())
ws = []
for i in range(n):
    ws.append(raw_input())

status = True
known = []

for i, w in enumerate(ws):
    if w in known:
        status = False
        break
    if w == "":
        status = False
        break
    if i !=0 and known[-1][-1] != w[0]:
        status = False
        break
    known.append(w)

if status:
    print("Yes")
else:
    print("No")
