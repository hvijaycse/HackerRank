

def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        Data = list( map( int, input().split()))
        Batteries = Data[1:]
        Batteries.sort()
        last_Battery = Batteries[0]
        Count = 1
        for battery in Batteries[1:]:
            New_battery = last_Battery | battery
            if New_battery == battery:
                Count = 0
            Count += 1
            last_Battery = New_battery
        print( Count)
if __name__ == "__main__":
    main()
    exit(0)