

def main():
    m = 1 << 128

    n, k = map(int, raw_input().split())
    x = map(int, raw_input().split())

    for i in range(0, n - k + 1):
        a = x[i]
        b = x[i - k + 1]

        if a < 0 < b:
            if abs(a) < abs(b):
                cost = abs(a) * 2 + abs(b)
            else:
                cost = abs(a) + abs(b) * 2
        else:
            cost = max(abs(a), abs(b))
        m = min(m, cost)
    print(m)

if __name__ == "__main__":
    main()
