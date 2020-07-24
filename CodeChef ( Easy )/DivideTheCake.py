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
        Angle = Int()
        if Angle < 361:
            if not 360 % Angle:
                if Angle > 26:
                    print( 'y y n')
                else:
                    print( 'y y y')
            else:
                if Angle > 26:
                    print( 'n y n')
                else:
                    print( 'n y y')
        else:
            print('n n n')

        

if __name__ == "__main__":
    main()
    exit(0)