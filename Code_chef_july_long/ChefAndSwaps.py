

def Solver( Array1, Array2):
    Dict1 = {}
    Dict2 = {}
    DictTotal = {}
    cost = 0
    i = 0
    N = len( Array1)
    j = N - 1

    for a in Array1:
        if a not in Dict1:
            Dict1[a] = 1
            DictTotal[a] =1
        else:
            Dict1[a] += 1
            DictTotal[a] += 1

    for b in Array2:
        if b not in Dict2:
            Dict2[b] = 1
        else:
            Dict2[b] += 1
        if b not in DictTotal:
            DictTotal[b] = 1
        else:
            DictTotal[b] += 1

    for num in DictTotal.keys():
        if DictTotal[num] % 2 != 0:
            return -1
    Array1.sort()
    Array2.sort()

    while i < N:
        while  i < N and Array1[i] == Array2[i]:
            i += 1
        while j > -1 and Array1[j] == Array2[j]:
            j -= 1
        if i < N:
            TopLeft, TopRight = Array1[i], Array1[j]
            BotLeft, BotRight = Array1[i], Array2[j]
            if Dict1[TopLeft] == Dict2[TopLeft]:
                TopLeftV = False
            else:
                TopLeftV = True

            if Dict1[TopRight] == Dict2[TopRight]:
                TopRightV = False
            else:
                TopRightV = True

            if Dict1[BotLeft] == Dict2[BotLeft]:
                BotLeftV = False
            else:
                BotLeftV = True

            if Dict1[BotRight] == Dict2[BotRight]:
                BotRightV = False
            else:
                BotRightV = True
            

            



def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        N = int( input() )
        A = list( map( int, input().split() ) )[ :N ]
        B = list( map( int, input().split() ) )[ :N ]
        Ans = Solver(A, B)
        print( Ans)

if __name__ == "__main__":
    main()
    exit(0)