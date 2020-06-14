
def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        N = int( input() )
        Matrix = [ [0]*N for i in range(N) ]
        ODD = []
        EVEN = []
        i = 1
        while i <= N*N:
            ODD.append(i)
            i += 2
        i = 2
        while i <= N*N:
            EVEN.append(i)
            i += 2
        row , column = N -2, -1
        if len( ODD) > len( EVEN):
            odder = True
        else:
            odder = False
        
        row , column = N -1 , 0
        for add in range(N):
            r = row - add 
            c = column 
            count = add + 1
            if odder:
                while count:
                    Matrix[r][c] = ODD.pop()
                    r = r + 1
                    c = c + 1
                    count -= 1
                odder = False
            else:
                while count:
                    Matrix[r][c] = EVEN.pop()
                    r = r + 1
                    c = c + 1
                    count -= 1
                odder = True

        row, column = 0, 1
        for add in range( N - 1):
            r = row 
            c = column + add
            count = N - 1 - add
            if odder:
                while count:
                    Matrix[r][c] = ODD.pop()
                    r = r + 1
                    c = c + 1
                    count -= 1
                odder = False
            else:
                while count:
                    Matrix[r][c] = EVEN.pop()
                    r = r + 1
                    c = c + 1
                    count -= 1
                odder = True

        
        for row in Matrix:
            for i in row:
                print(i, end = ' ')
            print()

if __name__ == "__main__":
    main()
    exit(0)