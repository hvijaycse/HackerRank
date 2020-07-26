def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))

def yes():
    print('YES')

def no():
    print('NO')

def main():
    TestCase = Int()
    for _ in range(TestCase):
        N, M = Ilist()
        Planets = Ilist()
        assert( N == len(Planets) )
        Planets.sort( reverse=True)
        if Planets[0] > M:
            print('impossible')
        else:
            last = Planets[0]
            Count = 1
            for i in range( 1, N):
                if last + Planets[i] > M:
                    last = Planets[i]
                    Count += 1
                    continue
                else:
                    break
            print(Count)
        
if __name__ == "__main__":
    main()
    exit(0)