

def main():
    TestCase = int( input() )
    for _ in range( TestCase):
        N = int( input() )
        S = list( map( int, input().split() ))
        S.sort()
        Min_Gap = float('inf')
        Index = 0
        while Index < N - 1:
            diff = S[ Index + 1] - S[ Index]
            if diff < Min_Gap:
                Min_Gap = diff
            Index += 1
        print( Min_Gap )

if __name__ == "__main__":
    main()
    exit(0)