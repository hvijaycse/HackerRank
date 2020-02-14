from time import clock

def Heapify( Index, Array):
    Length = len( Array)
    if Index > 0 and Index < Length: 
        Parent = Array[ Index ]
        while Index < Length :
            Minimum = Index
            Left = Index*2
            if Left < Length and Array[ Left]  < Array[ Minimum]:
                Minimum = Left
            Right = Left + 1
            if Right < Length and Array[ Right]  < Array[ Minimum]:
                Minimum = Right
            if Minimum != Index :
                Array[ Index] = Array[ Minimum]
                Index = Minimum
                continue
            break
        Array[ Index] = Parent

def Create_Min_Heap(Array):
    Array.append( Array[0] )
    Array[0] = float( '-inf')
    Length = len(Array)
    Index = Length >> 1 
    while Index :
        print( Index, end =  ' ')
        Heapify( Index, Array)
        Index = Index - 1

def Pop_Min( Array ):
    Last_element = Array.pop()
    Return_Element = Array[1]
    Array[1] = Last_element
    Heapify( 1, Array)
    return Return_Element

def Add_Element( Array, Element):
    Array.append( Element)
    Length = len( Array )
    Index = Length - 1
    Parent =  Index >> 1
    while Parent > 0 and  Array[ Parent] < Array[ Index]  :
        Array[ Index] = Array [ Parent]
        Index = Parent
        Parent = Index >> 1
    Array[ Index ] = Element
        
 
def cookies( Sweetness, Cookie_Array):
    operations = 0
    Create_Min_Heap( Cookie_Array)
    print( Cookie_Array)
    try:
        while Sweetness >= Cookie_Array[1]:
            Cookie1 = Pop_Min( Cookie_Array)
            print( Cookie_Array, end =' ')
            Cookie2 = Pop_Min( Cookie_Array)
            print( Cookie_Array, end =' ')
            Add_Element( Cookie_Array, ( Cookie1 + (Cookie2 << 1)))
            print( Cookie_Array)
            operations = operations + 1
        print( Cookie_Array)
        return operations
    except:
        return -1
            
    
if __name__ == "__main__":
    # file = open( 'J&C[Test_Case_12].txt' )
    file = open( 'new.txt' )
    nk = file.readline().strip().split()
    n = int(nk[0])
    k = int(nk[1])
    A = list(map(int, file.readline().rstrip().split()))
    start = clock()
    result = cookies( k, A)
    end=clock()
    print( result , 'Time Taken =', (end - start) )