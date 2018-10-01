S = raw_input()
maxl = 1
l = None
c = None
for i in S:
    if c == None:
        c = i
        l = 1
        continue
    if i == c:
        l += 1
        if maxl < l:
            maxl = l
    else:
        l = 1
        c = i
        continue
if maxl == 1:
    print(2)
else:
    print(maxl)


# for i in range(len(S)-1, 2, -1):
#     print(i, len(S)-i+1)
#     for j in range(len(S) -i+1):
#         l = [1] * j + [0] * i + [1] * (len(S)-j-i)
#         print(l)
