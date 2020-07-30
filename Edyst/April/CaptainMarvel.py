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
        Data = Ilist()
        N = Data[0]
        Data = Data[1:]
                    
if __name__ == "__main__":
    main()
    exit(0)