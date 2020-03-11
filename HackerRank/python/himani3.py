# cook your dish here
def Count( Array):
    Even = 0
    Odd = 0
    for number in Array:
        if number & 1:
            Odd = Odd + 1
        else:
            Even = Even + 1
    return [ str(Even), str(Odd)]

if __name__ == "__main__":
    Cases = int(input())
    while Cases:
        N, Q = map(int, input().split())
        Integers = list(map(int, input().strip().split()))[:N]
        Even, Odd = Count( Integers)
        queries = []
        while Q:
            Q = Q - 1
            queries.append( int(input()))
        Ans = []
        for query in queries:
            if query & 1:
                Ans.append( [Odd, Even])
            else:
                Ans.append( [Even,Odd])
        print( '\n'.join( [' '.join(Answer) for Answer in Ans ]  ) + '\n')
        Cases -= 1
    exit(0)