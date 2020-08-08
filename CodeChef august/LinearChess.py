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
        N, K = Ilist()
        Players = Ilist()
        Min_moves = float('inf')
        players_ans = -1
        for P in Players:
            if P <= K and K % P == 0 and K//P < Min_moves:
                Min_moves = K//P
                players_ans = P
        print( players_ans)
        

if __name__ == "__main__":
    main()
    exit(0)