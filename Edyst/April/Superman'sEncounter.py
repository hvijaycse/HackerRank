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
    Days = [
        'daxamday',
        'sunday',
        'monday',
        'tuesday',
        'wednesday',
        'thursday', 
        'friday',
        'saturday',
        'kryptonday',
        'coluday',
    ]
    for _ in range(TestCase):
        N = Int()
        N += 1
        N = N % 296
        N = N % 10
        print( Days[N])
        

if __name__ == "__main__":
    main()
    exit(0)