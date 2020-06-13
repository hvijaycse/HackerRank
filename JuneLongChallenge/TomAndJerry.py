def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        TS = int( input())
        while TS % 2 == 0 and TS >1:
            TS = TS//2
        print( TS // 2)

if __name__ == "__main__":
    main()
    exit(0)