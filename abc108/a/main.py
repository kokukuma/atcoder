n = input()

if n % 2 == 0:
    even = int(n / 2)
    odd = int(n / 2)
else:
    even = int(n / 2)
    odd = int(n / 2) + 1
print(even*odd)
