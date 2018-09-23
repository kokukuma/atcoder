N, M, X, Y = map(int, raw_input().split())
x = map(int, raw_input().split())
y = map(int, raw_input().split())

# if max(x) < min(y) and X < min(y) and max(x) < Y:
#     print("No War")
# else:
#     print("War")

for z in range(-100, 101):
    if X < z and z <= Y and max(x) < z and z <= min(y):
        print("No War")
        exit(0)
print("War")
