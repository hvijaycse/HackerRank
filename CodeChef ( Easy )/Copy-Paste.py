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
        N = Int()
        Array = Ilist()[: N]
        print( len( set( Array)) )
        

if __name__ == "__main__":
    main()
    exit(0)