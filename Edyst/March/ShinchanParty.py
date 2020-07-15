

def main():
    TestCase = int( input())
    Infinity = float('inf')
    while TestCase:
        TestCase -= 1
        N, N = map( int, input().split() )
        Grid = []
        for _ in  range( N):
            row = list( map( int, input().split() ))
            c = 0
            while c < N:
                if row[c]:
                    row[c] = Infinity
                c += 1
            Grid.append( row)

        r, c = 0, 1
        while c < N :
            Grid[r][c] = Grid[r][c - 1] + 1
            c += 1
                
        r,c = 1, 0
        while r < N :
            Grid[r][c] = Grid[r -1][c] + 1
            r += 1

        for r in range( 1, N):
            for c in range( 1, N):
                if Grid[r][c] != Infinity:
                    initial_value = Grid[r][c]
                    if not initial_value:
                        initial_value = Infinity
                    if r == c:
                        Daigonal = Grid[r - 1][ c - 1]
                    else:
                        Daigonal = Infinity
                    Grid[r][c] = min(
                        initial_value,
                        Grid[r - 1][c] + 1,
                        Grid[r][ c - 1] + 1,
                        Daigonal + 1
                    ) 

        print( Grid[N -1 ][ N - 1])

         

if __name__ == "__main__":
    main()
    exit(0)