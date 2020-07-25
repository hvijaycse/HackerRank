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
    Character = [ chr(i) for i in range(65 , 75)]
    for _ in range(TestCase):
        Hour, Minute = map( int, input().split(':'))
        Sum = Hour
        for _ in range( Minute):
            Hour = 2 * Hour - 1
            Sum += Hour
        Code = []
        while Sum:
            number = Sum % 10
            Code.append( Character[number])
            Sum = Sum //10
        Code.reverse()
        print(''.join( Code))


if __name__ == "__main__":
    main()
    exit(0)