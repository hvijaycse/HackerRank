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

def Mindiff( Number ):
    min1 = Number - 1
    i = 1
    for i in range( 1, int( Number ** 0.5) + 1):
        if not Number % i:
            if abs( (Number // i) - i) < min1:
                min1 = abs( (Number //i) - i)
    return min1
def main():
    TestCase = Int()
    for _ in range(TestCase):
        N = Int()
        print( Mindiff(N))


if __name__ == "__main__":
    main()
    exit(0)