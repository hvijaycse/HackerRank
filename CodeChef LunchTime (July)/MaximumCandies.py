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
        ans = 0
        N, M, X, Y = Ilist()
        if X <= Y //2:
            ans = N*M*X
        else:
            if N == 1 and M == 1:
                ans = X
            else:
                if M == 1:
                    N, M = M, N
                Max_elm = min( X, Y)
                Min_elm = min( Y - Max_elm, Y -1 )
                Max_row = (Max_elm + Min_elm)*( M //2) + Max_elm*( M %2)
                Min_row = (Max_elm + Min_elm)*( M //2) + Min_elm*( M %2)
                Two_rows = Max_row + Min_row
                ans = Two_rows*( N //2 ) + Max_row*( N % 2)

        print(ans)

if __name__ == "__main__":
    main()
    exit(0)