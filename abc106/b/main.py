n = int(raw_input())

count = 0
for i in range(1, n+1):
    if i % 2 == 0:
        continue

    c = 0
    for j in range(1, n+1):
        if i % j == 0:
            c += 1
    if c == 8:
        count += 1
print(count)
