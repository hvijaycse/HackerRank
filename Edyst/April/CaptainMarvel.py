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
        Data = Ilist()
        N = Data[0]
        Data = Data[1:]
        GreaterOnRight = [-1 for i in range(N)]
        SmallerOnLeft = [-1 for i in range(N)]
        Greatest = Data[N -1]
        for i in range( N -2, -1, -1):
            if Data[i] < Greatest:
                GreaterOnRight[i] = Greatest
            else:
                Greatest= Data[i]
        MaxAns = float('-inf')
        SmallList = [ Data[0] ]
        for i in range( 1, N):
            if GreaterOnRight[i] != -1:
                if Data[i] != SmallList[0] and Data[i] < SmallList[0]:
                    SmallList = [Data[i]] + SmallList
                else:
                    start = 0
                    end = len( SmallList)
                    while start != end:
                        mid = (start + end) //2
                        if SmallList[mid] == Data[i]:
                            mid -= 1
                            break
                        elif Data[i] < SmallList[mid]:
                            end = mid
                            continue
                        else:
                            start = mid + 1
                    while mid > -1 and SmallList[mid] > Data[i]:
                        mid -= 1
                    if mid > -1 :
                        SmallerOnLeft[i] = SmallList[mid]
                    if Data[i] not in SmallList:
                        SmallList.append( Data[i])
                        SmallList.sort()
                    value = SmallerOnLeft[i] - Data[i] + GreaterOnRight[i]
                    if value > MaxAns:
                        MaxAns = value
        print( MaxAns)

                    
if __name__ == "__main__":
    main()
    exit(0)