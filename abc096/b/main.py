a, b, c = map(int, raw_input().split())
k = int(raw_input())
max_value = max([a,b,c])
value = max_value
for i in range(k):
    value = value * 2
print(sum([a,b,c]) - max_value + value)
