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
        N , K = Ilist()
        Distance = Ilist()[:N]
        for Dis in Distance:
            if Dis % K:
                print('0', end='')
            else:
                print('1',end='')
        print()
        

if __name__ == "__main__":
    main()
    exit(0)