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

def getTime(Array):
    Times = {}
    for row in Array:
        x, y , v = row
        time = (x**2+ y**2)/(v ** 2)
        if time in Times:
            Times[time] += 1
        else:
            Times[time] = 1
    return Times
def main():
    C = Int()
    Cars = []
    for _ in range(C):
        Row = Ilist()
        Cars.append( Row)
    Times = getTime(Cars)
    Count = 0 
    for value in Times.values():
        Count += (value *(value -1))//2
    print( Count)


if __name__ == "__main__":
    main()
    exit(0)