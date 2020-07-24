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
        L, D, S, C = Ilist()
        # final_likes = S * (Multiple ** (D - 1))
        for _ in range( D - 1):
            S = S*(C + 1)
            if S >=L:
                break
        if S >= L:
            print('ALIVE AND KICKING')
        else:
            print('DEAD AND ROTTING')
        

if __name__ == "__main__":
    main()
    exit(0)