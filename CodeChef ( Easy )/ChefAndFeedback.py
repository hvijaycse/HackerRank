def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))


def main():
    TestCase = Int()
    for _ in range( TestCase ):
        S = input()
        if '010' in S or '101' in S:
            print(' Good')
        else:
            print( 'Bad') 

if __name__ == "__main__":
    main()
    exit(0)