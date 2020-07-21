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
        if N and K:
            print(
                N // K,
                N % K
            )
        else:
            print( 0, N)
        

if __name__ == "__main__":
    main()
    exit(0)