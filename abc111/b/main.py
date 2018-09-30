N = map(int, list(raw_input()))

if N[0] > N[1]:
    l = [N[0]] * 3
    print(''.join([str(i) for i in l]))
elif N[0] == N[1] >= N[2]:
    l = [N[0]] * 3
    print(''.join([str(i) for i in l]))
elif N[0] == N[1] < N[2]:
    l = [N[0]+1] * 3
    print(''.join([str(i) for i in l]))
elif N[0] < N[1]:
    l = [N[0]+1] * 3
    print(''.join([str(i) for i in l]))


