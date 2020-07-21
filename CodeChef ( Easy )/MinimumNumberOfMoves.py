def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))


def main():
    TestCase = Int()
    for _ in range( TestCase ):
        N = Int()
        Workers = Ilist()
        first = 0; last = len(Workers) - 1 
        Count = 0
        if N != 1:
            Workers.sort()
            while Workers[ first] != Workers[ last ]:
                diff = Workers[ last ] - Workers[ first ]
                Count += diff
                for index in range( first, last):
                    Workers[ index ] += diff
                tmpL = last
                while (tmpL - 1 > -1  ) and (Workers[ tmpL - 1] > Workers[tmpL]):
                    Workers[tmpL - 1], Workers[tmpL] = Workers[ tmpL], Workers[ tmpL - 1]
                    tmpL -= 1
        print( Count)


if __name__ == "__main__":
    main()
    exit(0)