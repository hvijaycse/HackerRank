
def Solver( array):
    Correct_index = {}
    Backward_indexes = []
    Sort_arr = sorted(array)
    steps = 0
    Changes = []
    for index, value in enumerate( Sort_arr):
        Correct_index[value] = index
    for index, value in enumerate( array):
        if Correct_index[value] - index < 0:
            Backward_indexes.append( index)
    while Backward_indexes[1:]:
        steps += 1
        First = Backward_indexes[0]
        Last = Backward_indexes[-1]
        Replace_index = Correct_index[array[Last]]
        Changes.append( [Replace_index, First, Last ])
        Change = ( array[Last], array[Replace_index], array[First])
        array[ Replace_index], array[First], array[Last] = Change
        if Correct_index[ array[First]] - First < 0 :
            continue
        Backward_indexes = Backward_indexes[1:]
    Forward_index = []
    f = 0
    for index, value in enumerate( array):
        if Correct_index[value] - index > 0 :
            f += 1
            Forward_index.append(index)
    if f != 2 :
        return -1, []
    Changes.append( [Forward_index[0], Forward_index[1], Backward_indexes[0]] )
    Change = ( array[ Backward_indexes[0]], array[Forward_index[0]], array[Forward_index[1]])
    array[Forward_index[0]], array[Forward_index[1]], array[Backward_indexes[0]] = Change
    steps += 1
    return steps, Changes
        
        
if __name__ == "__main__":
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N, K = map( int, input().split())
        array = list( map( int, input().split()))
        Count, Change = Solver( array)
        if Count > K or Count == -1:
            print('-1')  
            continue
        print( Count)
        for step in Change:
            print( step[0] + 1, step[1] + 1, step[2] + 1)
        
            
        