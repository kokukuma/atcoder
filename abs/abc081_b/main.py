def main():
    n = map(int, raw_input().split())
    x = map(int, raw_input().split())

    c = 0
    while True:
        for i in x:
            if i % 2 != 0:
                print(c)
                return
        c += 1
        x = [ i/2 for i in x]

if __name__ == "__main__":
    main()
