# from math import comb

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

def comb(Num , A):
    B = Num - A
    if A > B:
        B, A = A, B
    numerator = 1
    for i in range(B+1, Num + 1):
        numerator *= i
    denominator = 1
    for i in range( 2, A + 1):
        denominator *= i
    
    return numerator // denominator


def main():
    TestCase = Int()
    for _ in range(TestCase):
        Possible = True
        Ax, Ay = Ilist()
        Bx, By = Ilist()
        Allowed = input()

        if Allowed[0] == 'N':
            if Ay > By:
                Possible = False
        else:
            if Ay < By:
                Possible = False
        if Allowed[1] == 'E':
            if Ax > Bx:
                Possible = False
        else:
            if Ax < Bx:
                Possible = False
        
        if Possible:
            Xmoves = abs(Ax - Bx)
            Ymoves = abs( Ay - By)
            ans = 'Total Ways: '+ str(comb( Xmoves + Ymoves, Xmoves))
        else:
            ans = 'impossible'
        print( ans)

if __name__ == "__main__":
    main()
    exit(0)