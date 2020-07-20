def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))


def main():
    TestCase = Int()
    for _ in range( TestCase):
        Lucky = False
        Total_page, Current_page, Budget, Options = map( int, List())
        Remaining = Total_page - Current_page
        for _ in range( Options):
            Pages, Price = map(int, List() )
            if Remaining <= Pages and Price <= Budget:
                Lucky = True
        if Lucky:
            print('LuckyChef')
        else:
            print('UnluckyChef')

            

if __name__ == "__main__":
    main()
    exit(0)