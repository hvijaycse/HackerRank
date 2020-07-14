
def main():
    AlphaDict = {}
    for i in range(1, 26):
        AlphaDict[i] = chr( i + 96)
    AlphaDict[0] = 'z'
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        Data = list( map( int, input().split() ) )
        N = Data[0]
        Grid = [ Data[i : i + N] for i in range(2, N*N + 1, N)]
        row = N + 1
        Subract = True
        Password = []
        for column in range( N):
            if Subract:
                row -= 2
                num = Grid[ row][column]
                if not row:
                    Subract = False
            else:
                row += 2
                num = Grid[ row][ column]
            Password.append( 
                AlphaDict[ num % 26 ]
            )
        print( ''.join( Password))


if __name__ == "__main__":
    main()
    exit(0)