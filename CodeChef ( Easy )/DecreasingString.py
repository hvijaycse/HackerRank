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
    string = [chr(122 - i) for i in range( 26) ]
    for _ in range(TestCase):
        K = Int()
        ans = []
        Times = K // 25
        Remain = K % 25
        if Times:
            ans = [character for character in string]
        for _ in range(Times -1):
            ans = string +  ans
        if Remain:
            ans =  string[25 - Remain:] + ans
        print(''.join(ans))
            

if __name__ == "__main__":
    main()
    exit(0)