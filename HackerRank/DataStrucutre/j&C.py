
def Bubble_Up( heap, Start_pos, pos):
    newitem = heap[ pos]
    while pos > Start_pos:
        Parent_Index = pos >> 1
        Parent = heap[ Parent_Index]
        if newitem < Parent:
            heap[ pos] = Parent
            pos = Parent_Index
            continue
        break
    heap [pos] = newitem
        
def Min_Heapify( heap, index):
    if index == 0 :
        return
    End_pos = len( heap )
    New_Elemenet = heap[ index ]
    Start_pos = index
    Child = index << 1
    while Child < End_pos:
        Right =  Child + 1
        if Right < End_pos and heap[ Child] > heap[ Right]:
            Child = Right
        heap[ index] = heap[ Child]
        index = Child
        Child = Child << 1          
    heap[ index] = New_Elemenet
    Bubble_Up( heap, Start_pos, index)
    return

def Create_Heap( heap):
    heap.append( heap[0])
    heap[0] = float('-inf')
    Length = len( heap)
    Length = Length >> 1
    while Length:
        Min_Heapify( heap, Length)
        Length = Length - 1
    return

def PoP_Min( heap):
    Return_element = heap[1]
    Last_Element = heap.pop()
    if len( heap) == 1:
        return Return_element
    heap[1] = Last_Element
    Min_Heapify(heap, 1)
    return Return_element

def Add_element( heap, Element):
    heap.append( Element)
    Length = len( heap)
    Parent = Length >> 1
    Child = Length - 1
    while heap[ Parent] > Element :
        heap[ Child] = heap[ Parent]
        Child =  Parent
        Parent  =  Parent >> 1
    heap[ Child] = Element
    
def cookies( Min_swetness, cookie_array ):
    operations = 0
    try:
        Create_Heap( cookie_array)
        while Min_swetness > cookie_array[1]:
            operations = operations + 1
            C1 =  PoP_Min( cookie_array)
            C2 =  PoP_Min( cookie_array)
            Add_element( cookie_array, ( C1 +( C2 << 1) ))
            # print( cookie_array[:-20])
        return operations
    except:
        return -1
    
if __name__ == "__main__":
    file = open( 'J&C[Test_Case_12].txt' )
    # file = open( 'new.txt' )
    nk = file.readline().strip().split()
    n = int(nk[0])
    k = int(nk[1])
    A = list(map(int, file.readline().rstrip().split()))
    result = cookies( k, A)
    print( result)