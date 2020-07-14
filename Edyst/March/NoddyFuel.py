

def Check( Stations, Target_Fuel):
    if not Stations:
        return False
    if Target_Fuel in Stations:
        return True
    for i in range( 1, Target_Fuel):
        if i in Stations:
            Stations.remove(i)
            if Check( Stations, Target_Fuel - i ):
                return True
            else:
                Stations.append(i)
    return False

def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        Data = list( map( int, input().split()))
        Target_Fuel = int( input() )
        Limit = int( input() )
        Stations = Data[1:]
        for index in range( len( Stations) ):
            if Stations[index] > Limit:
                Stations[index] = Limit
        if sum( Stations) >=Target_Fuel and  Check( Stations, Target_Fuel):
            print('Yes')
        else:
            print('No')

        

if __name__ == "__main__":
    main()
    exit(0)