
def main():
    TestCase = int( input())
    while TestCase :
        TestCase -= 1
        Game = int( input())
        while Game:
            Game -= 1
            I , N , Q = map( int, input().split())
            if N % 2:
                if I == Q:
                    print(N //2)
                else:
                    print( (N//2) + 1)
            else:
                print( N//2)
    return

if __name__ == "__main__":
    main()
    exit(0)