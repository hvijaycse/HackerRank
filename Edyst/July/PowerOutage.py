def Int():
    return int( input() )

def Listing():
    return input().split()

def Ilist():
    return list( map( int, input().split()))

def yes():
    print('YES')

def no():
    print('NO')

def main():
    R1 = float(input())
    Striker, NonStriker = Ilist()
    Runs = Listing()
    B1 = len(Runs)
    R2 = float(input())
    Gain = 0
    for  run in  Runs:
        if run != 'W':
            run = int( run )
            Gain += run
    TotalRun = int(((B1*R2 - 6*Gain)*R1)/(6*( R1 - R2)))
    if R1 == 0:
        Ib = 0 
    else:
        Ib = (6*TotalRun)//R1
    Ib = Ib%6
    for run in Runs:
        if run == 'W':
            Striker = 0
        else:
            run = int( run)
            Striker += run
            if run%2:
                Striker, NonStriker = NonStriker, Striker
        Ib += 1
        if (Ib )%6 == 0 :
            Striker, NonStriker = NonStriker, Striker
    print( TotalRun+ Gain, Striker, NonStriker)

        
        

if __name__ == "__main__":
    main()
    exit(0)