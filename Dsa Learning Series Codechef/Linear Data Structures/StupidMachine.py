
def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int(input())
        S = list( map( int, input().split()))[ :N]
        S_min = [ S[0] ]
        for i in range( 1, N):
            if S[i] < S_min[i -1]:
                S_min.append( S[i])
            else:
                S_min.append( S_min[i - 1])
        Total = 0
        i = N -1
        last_min = 0
        while i >= 0:
            Total += ( S_min[i] - last_min ) * ( i + 1)
            last_min = S_min[i]
            i -= 1
            while i >= 0 and S_min[i] == S[i + 1]:
                i -= 1
        print(Total)

    return

if __name__ == "__main__":
    main()
    exit(0)