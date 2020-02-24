def Dating( Before, Stack):
    print( Before, Stack)
    Max_Days = 0
    while Stack:
        TOP = Stack.pop()
        if TOP <= Before:
            Before = TOP
        else:
            TO_Be_Breaked = False
            Days = 1
            MINI = []
            Biggest = TOP
            while Stack:
                New = Stack.pop()
                if New <= Before:
                    Before = New
                    break
                if New <= Biggest:
                    MINI.append( New)
                    Days = Days + 1
                else:
                    TO_Be_Breaked = True
                Biggest = New
            if TO_Be_Breaked:
                MINI.reverse()
                Days = 1 + Dating( Before, MINI)
            if Days > Max_Days:
                Max_Days = Days
    return Max_Days


if __name__ == "__main__":
    # file = open('32400.txt')
    # Number = int(file.readline())
    Number = int( input() )
    # start = time()
    Plants =  list( map(int, input().split() ) )
    # Plants =  list( map(int, file.readline().split() ) )
    Max_Days = 0
    Plants.reverse()
    Before = Plants.pop()
    Days = Dating(Before, Plants)
    print(Days)