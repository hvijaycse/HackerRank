
def Solver( array, K):
    steps = 0
    Sorted_arr = sorted( array)
    Correct_index = {}
    for index, value in enumerate( Sorted_arr):
        Correct_index[ value] = index
    Backward = []
    for index, value in enumerate( array):
        if Correct_index[value] - index < 0 :
            Backward.append(index)
    ABC = ''
    while K and Backward[1:]:
        steps += 1
        K -=1 
        Last_val , Last_index = array[Backward[-1]], Backward[-1]
        First_val, First_index = array[Backward[0]], Backward[0]
        Position = Correct_index[ Last_val]
        Forward = array[Position]
        array[Position], array[ First_index], array[ Last_index] = Last_val, Forward, First_val
        ABC += str(Position + 1) + ' ' + str( First_index + 1) + ' ' + str( Last_index + 1) + '\n'
        if Correct_index[Forward] - First_index < 0:
            continue
        else:
            Backward = Backward[1:]
    
    if K  :
        Forward = []
        for index, value in enumerate( array):
            if Correct_index[value] - index > 0:
                Forward.append( index)
        if len( Forward) != 2:
            return '', -1
        Last_val , Last_index = array[Backward[-1]], Backward[-1]
        First_val, First_index = array[Forward[-1]], Forward[-1]
        Position = Correct_index[ Last_val]
        F_Value = array[Position]
        array[Position], array[First_index], array[Last_index] = Last_val, F_Value, First_val
        ABC += str(Position + 1) + ' ' + str( First_index + 1) + ' ' + str( Last_index + 1) + '\n'
        return ABC, steps + 1
        
    else:
        return '', -1
        
if __name__ == "__main__":
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N, K = map( int, input().split())
        array = list( map( int, input().split()))
        ans , steps  = Solver( array, K)
        print( steps)
        if steps != -1 :
            print( ans)
    exit(0)