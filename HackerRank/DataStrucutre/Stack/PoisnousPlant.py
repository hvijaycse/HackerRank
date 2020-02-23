if __name__ == "__main__":
    # file = open('32400.txt')
    # Number = int(file.readline())
    Number = int( input() )
    # start = time()
    Plants =  list( map(int, input().split() ) )
    # Plants =  list( map(int, file.readline().split() ) )
    Max_Days = 0
    Must = Plants[0]
    Index = 1
    Last = Number
    Prev_MIn = float('-inf')
    flag = False
    while Index < Last:
        if Plants[Index] <= Must:
            Must = Plants[Index]
            Index += 1
        else:
            Days = 1
            while  Index + 1 < Last and Plants[Index + 1] > Plants[Index]:
                Index = Index + 1
            while Index + 1 < Last and Plants[Index + 1] >= Must and Plants[Index + 1] < Plants[Index]:
                flag = True
                Last_Min = Plants[ Index + 1]
                Index = Index + 1
                Days = Days + 1
            Index += 1
            if flag:
                if Last_Min < Prev_MIn:
                    Days = Days + 1
                Prev_MIn = Last_Min
            if Days > Max_Days:
                Max_Days = Days
    print(Max_Days)