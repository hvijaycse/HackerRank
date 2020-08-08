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
        H, P = Ilist()
        tmp_p = 0
        while P:
            tmp_p += P
            P = P //2
        if tmp_p >= H:
            print(1)
        else:
            print(0)
        

if __name__ == "__main__":
    main()
    exit(0)