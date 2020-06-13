
def Solver( array, K):
    steps = 0
    Backward = []
    Forward = []
    F_or_B = {}
    Possible = True
    Correct_index = {}
    changes = ''
    Sorted_arr = sorted( array)
    for index, value in enumerate( Sorted_arr):
        Correct_index[ value] = index
    for index, value in enumerate( array):
        if Correct_index[value] - index > 0 :
            Forward.append(index)
            F_or_B[value] = True
        elif Correct_index[value] - index < 0 :
            Backward.append(index)
            F_or_B[value] = True
    while Backward and Possible:
        steps += 1
        F_last =  Forward.pop()
        B_last = Backward.pop()
        Going_index = Correct_index[array[B_last]]
        last_value = array[Going_index]
        array[Going_index], array[F_last], array[B_last] = ( array[B_last], array[Going_index], array[F_last])
        changes += str( Going_index) + ' ' + str( F_last) + ' ' + str( B_last) + '\n'
        if F_or_B[last_value]:
            Forward.pop( Forward.index( last_value))
        else:
            Backward.pop( Backward.index( last_value))
        if Correct_index[value] - F_last < 0 :
            Backward.append( F_last)
            F_or_B[value] = False
        if steps > K:
            Possible = False
    if not Possible:
        return -1, ''
    else:
        return steps, changes
    
    
        
         
        
if __name__ == "__main__":
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N, K = map( int, input().split())
        array = list( map( int, input().split()))
        steps, ans  = Solver( array, K)
        print( steps)
        if steps != -1 :
            print( ans)
    exit(0)