

if __name__ == "__main__":
    TestCase = int( input())
    Index = {}
    for i in range( 97, 97+26):
        Index[chr(i)] = i -97
    while TestCase:
        TestCase -= 1 
        N , Q = map(int, input().split())
        String = [ cha for cha in input()]
        Counts = {}
        for s in String:
            if s not in Counts:
                Counts[s] = 1
            else:
                Counts[s] += 1
        values = list( Counts.values() )
        values = sorted(values, reverse = True)
        for q in range( Q):
            ans = 0
            query = int(input())
            for value in values:
                if value > query:
                    ans += value - query
                else:
                    break
            print( ans)
    exit(0)
            