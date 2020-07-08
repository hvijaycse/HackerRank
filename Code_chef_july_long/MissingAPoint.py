
def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int( input() )
        X = {}
        Y = {}
        for i in range( (4* N) - 1):
            xi, yi = map( int, input().split())

            if xi not in X:
                X[ xi ] = [ yi ]
            else:
                X[ xi ].append( yi )
            
            if yi not in Y:
                Y[ yi ] = [ xi ]
            else:
                Y[ yi ].append( xi )
        for x in X.keys():
            if len( X[x] ) % 2 != 0:
                Xans = x
                break
        for y in Y.keys():
            if len( Y[y]) % 2 != 0:
                Yans = y
                break
        print( Xans, Yans) 
        

if __name__ == "__main__":
    main()
    exit(0)