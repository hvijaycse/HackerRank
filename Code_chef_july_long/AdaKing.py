
def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int( input() )
        Board = [ [ '.' for i in range(9)] for j in range(9)]
        Board[0][0] = 'O'
        if N <= 8:
            for i in range( N + 1):
                Board[1][i] = 'X'
            Board[0][i] = 'X'
        else:
            row = N //8
            column = N % 8
            if column:
                for i in range( column + 1):
                    Board[row + 1][i] = 'X'
            for i in range( column , 9):
                Board[row][i] = 'X'
        for i in range(8):
            print( ''.join( Board[i][:8]) )
        print()

if __name__ == "__main__":
    main()
    exit(0)