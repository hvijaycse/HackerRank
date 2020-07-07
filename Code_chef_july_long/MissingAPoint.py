
def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int( input() )
        Points = []
        for i in range( N - 1):
            x, y = map( int, input().split())
            Points.append([ x, y])
        

if __name__ == "__main__":
    main()
    exit(0)