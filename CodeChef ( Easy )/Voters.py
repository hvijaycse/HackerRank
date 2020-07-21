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
    N1, N2, N3 = Ilist()
    CountDict = {}
    for _ in range( N1):
        Num = Int()
        CountDict[ Num] = 1
    for _ in range( N2):
        Num = Int()
        if Num in CountDict:
            CountDict[Num] = 2
        else:
            CountDict[Num] = 1
    for _ in range( N3):
        Num = Int()
        if Num in CountDict:
            CountDict[ Num] = 3
    Final_list = []
    for Value, time in CountDict.items():
        if time >1:
            Final_list.append( Value)
    Final_list.sort()
    print( len( Final_list ))
    for Value in Final_list:
        print( Value)        

if __name__ == "__main__":
    main()
    exit(0)