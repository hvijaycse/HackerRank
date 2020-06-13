def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int(input())
        Customers = list( map( int, input().split()))[:N]
        Five , Ten, Fifteen = 0, 0, 0
        index = 0
        CanSell = True
        while index < len( Customers) and CanSell:
            if Customers[index] == 5:
                Five += 1
            elif Customers[index] == 10:
                if not Five:
                    CanSell = False
                else:
                    Five -= 1
                Ten += 1
            else:
                if Ten > 0:
                    Ten -= 1
                elif Five >1:
                    Five -= 2
                else:
                    CanSell = False
                Fifteen += 1
            index += 1
        if CanSell:
            print( 'YES')
        else:
            print('NO')
    return

if __name__ == "__main__":
    main()
    exit(0)