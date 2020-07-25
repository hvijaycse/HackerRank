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

def ConvBinary( num ):
    string = ''
    while num:
        string = str( num % 2) + string
        num = num // 2
    return string

def integer( string ):
    num = 0
    for i in range( 1, len( string) + 1):
        if string[ -1*i ] == '1':
            num += 2**(i - 1)
    return num



def main():
    TestCase = Int()
    for _ in range(TestCase):
        N = Int()
        Numbers = Ilist()
        assert( N == len(Numbers))
        Binary = []
        for num in Numbers:
            Binary.append( ConvBinary( num ) )
        Maximum = float('-inf')
        for index, A in enumerate( Binary):
            for B in Binary[index + 1:]:
                AplusB =  integer(A + B)
                BplusA = integer( B + A)
                if Maximum < abs( AplusB - BplusA):
                    Maximum = abs(AplusB - BplusA)
        print( Maximum)
        

if __name__ == "__main__":
    main()
    exit(0)