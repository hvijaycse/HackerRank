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

def getNumber( Power):
    num1 = Power//9
    if Power%9:
        num1 += 1
    return num1

def main():
    TestCase = Int()
    for _ in range(TestCase):
        Pc, Pr = Ilist()
        ChefNumber = getNumber( Pc)
        RickNumber = getNumber( Pr)
        if ChefNumber >= RickNumber:
            print( 1, RickNumber)
        else:
            print(0 , ChefNumber)

        

if __name__ == "__main__":
    main()
    exit(0)