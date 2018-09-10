def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

N = int(raw_input())
prime = []
for i in range(2, 55555):
    if is_prime(i):
        prime.append(i)

for i in range(N):
    print prime[i],

