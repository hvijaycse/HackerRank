
def largestRectangle( Homes , floor, Start, End):
    if Start >= End:
        return 0
    Leveled_House = []
    Minimum_House = min( Homes[Start : End ] )
    if not Minimum_House:
        return 0
    Area = ( Minimum_House + floor) *( End - Start)
    floor = floor + Minimum_House
    for i in range( Start, End):
        Homes[i] = Homes[i] - Minimum_House
        if not Homes[i] :
            Leveled_House.append(i)
    for Indexes in Leveled_House:
        Current_Area = largestRectangle( Homes, floor, Start, Indexes)
        if Current_Area > Area:
            Area = Current_Area
        Start = Indexes + 1
    Current_Area = largestRectangle( Homes, floor, Start, End)
    if Current_Area > Area:
        Area = Current_Area
    return Area
                
    
    
if __name__ == '__main__':
    Number = int(input())
    Homes = list( map(int, input().split()))
    Max_Area = largestRectangle( Homes, 0, 0, Number)
    print(Max_Area)
    exit(0)