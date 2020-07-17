
def GetSet(Num):
    setbit = set()
    mask = 1
    for pos in range(0, 32):
        if ( mask << pos) & Num:
            setbit.add( pos)
    return setbit

def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        Data = list( map( int, input().split()))
        Batteries = Data[1:]
        allSet = []
        maxOR = 0
        for Battery in Batteries:
            maxOR = maxOR | Battery
            allSet.append( GetSet( Battery))
        MaxSet = GetSet( maxOR)
        Covered = set()
        AnswerSet = []
        while len( Covered) != len( MaxSet): # Using Len cause it will consume O(1) time not O(n)
            MaxDiff = max(
                allSet,
                key = lambda x: len( x- Covered)
            )
            Covered = Covered | MaxDiff
            AnswerSet.append( MaxDiff)
        print( len( AnswerSet))


        
 
if __name__ == "__main__":
    main()
    exit(0)