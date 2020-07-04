
def minus(a, b):
    if a - b < 0:
        return b - a - 1
    else:
        return a - b - 1

def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int( input())
        String = list( map( int, input().split()))[: N]
        Skips = 0
        i = 1
        while i < N:
            Skips += minus( String[i -1], String[i])
            i += 1
        print( Skips)
    return

if __name__ == "__main__":
    main()
    exit(0)