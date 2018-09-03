a, b, c = map(int, raw_input().split())
max_value = max([a,b,c])

target_value = max_value
while True:
    if (target_value*3 - (a+b+c)) % 2 == 0:
        break
    target_value += 1

diff_a = (target_value - a)
diff_b = (target_value - b)
diff_c = (target_value - c)

if diff_a % 2 == 0 and diff_b % 2 == 0 and diff_c % 2 == 0:
    count = diff_a / 2 + diff_b / 2 + diff_c / 2
    print(count)
else:
    count = diff_a / 2 + diff_b / 2 + diff_c / 2 + 1
    print(count)
