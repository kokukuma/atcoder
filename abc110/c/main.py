S = list(raw_input())
T = list(raw_input())
# print(S, len(S), len(set(S)))
# print(T, len(T), len(set(T)))

corr = {}
for i, s in enumerate(S):
    if s in corr.keys() and corr[s] != T[i]:
        print("No")
        exit(0)
    corr[s] = T[i]

corr = {}
for i, t in enumerate(T):
    if t in corr.keys() and corr[t] != S[i]:
        print("No")
        exit(0)
    corr[t] = S[i]

print("Yes")
