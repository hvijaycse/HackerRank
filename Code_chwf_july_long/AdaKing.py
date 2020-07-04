

def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        N = int( input() )
        Board = [ [ '.' for i in range(9)] for i in range(9)]
        Board[0][0] = 'O'
        if N <= 8 :
            for i in range(0, N):
                Board[1][i] = 'X'
            Board[1][i + 1] = 'X'
            Board[0][i + 1] = 'X'
        else:
            j = N //8 + 1
            k = N % 8
            for i in range( k + 1):
                Board[j][i] = 'X'
            for i in range( k + 1, 9):
                Board[j - 1][i] = 'X'
        for i in range(8):
            print( ''.join( Board[i][:8] ))
        print()
    return

if __name__ == "__main__":
    main()
    exit(0)