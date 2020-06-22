def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int( input())
        Cars = list( map( int, input().split()[:N]))
        Count = 1 
        Max_speed = Cars[0]
        for speed in Cars[1:]:
            if speed <= Max_speed:
                Max_speed = speed
                Count += 1
        print( Count )
    return

if __name__ == "__main__":
    main()
    exit(0)