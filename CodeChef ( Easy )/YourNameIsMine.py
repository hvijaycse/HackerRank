def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))

def yes():
    print('YES')

def no():
    print('NO')

def main():
    TestCase = Int()
    for _ in range(TestCase):
        M , W = List()
        if len(M) > len(W):
            M, W = W, M
        MI = 0
        WI = 0
        WLimit = len( W)
        MLimit = len( M)
        while  MI < MLimit and WI < WLimit:
            while WI < WLimit and  M[MI] != W[WI]:
                WI += 1
            if WI < WLimit and M[MI] == W[WI]:
                MI += 1
                WI += 1
            else:
                break
        if MI == MLimit and M[MI -1] == W[WI -1]:
            yes()
        else:
            no()

if __name__ == "__main__":
    main()
    exit(0)