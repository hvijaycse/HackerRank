def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))


def main():
    TestCase = Int()
    for _ in range( TestCase ):
        N = Int()
        Array = Ilist()
        Possible = True
        if N > 2:
            Local = 0
            Global = 0

            for upto in range( 1, N):
                for index in range( upto):
                    if Array[index] > Array[upto]:
                        Local += 1
            for index in range( 1, N):
                if Array[index - 1] > Array[ index]:
                    Global += 1
            if Global != Local:
                Possible = False
        if Possible:
            print('YES')
        else:
            print('NO')

if __name__ == "__main__":
    main()
    exit(0)