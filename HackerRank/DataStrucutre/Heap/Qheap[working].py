class Heap():
    
    def __init__( self ):
        self.HeapLength = 0
        self.Heap_Array = [ float( '-inf' ) ] 
    
    def Heap_minimum( self ):
        return self.Heap_Array[1]
    
    def parent(self, Index ):
        return Index//2
    
    def left(self, Index ):
        return Index*2
    
    def right(self, Index ):
        return 2*Index + 1 
    
    def swap(self, index_1, index_2):
        temp=self.Heap_Array[ index_1 ]
        self.Heap_Array[ index_1 ] = self.Heap_Array[ index_2 ]
        self.Heap_Array[ index_2 ] = temp
        return
    
    
    
    def Update_key( self, Index, Element ):
        if Element > self.Heap_Array[Index]:
            print( "The elemnt is already smaller than the index value" )
        else:
            self.Heap_Array[ Index ] = Element
            while Index >= 1 and self.Heap_Array[ self.parent( Index ) ] > Element:
                self.swap( Index, self.parent( Index )) 
                Index=self.parent( Index )
            
    def Add_Element( self, Element ):
        self.HeapLength = self.HeapLength + 1
        self.Heap_Array.append( float( '+inf' ) )
        self.Update_key( self.HeapLength, Element)
        return
    
    def Heapify( self, Index):
        minimum=Index
        left = self.left( Index )
        right = self.right( Index )
        if  left < self.HeapLength and  self.Heap_Array[ Index ] > self.Heap_Array[ left ]:
            minimum=left
        if  right < self.HeapLength and self.Heap_Array[ minimum ] > self.Heap_Array[ right ]:
            minimum=right
        if minimum != Index:
            self.swap( Index, minimum)
            self.Heapify( minimum )
        return
        
    
    def Delete_Element(self, Element):
        Index = self.Heap_Array.index( Element )
        if  Element > self.Heap_Array[ self.HeapLength ] :
            self.Update_key( Index, self.Heap_Array[ self.HeapLength ])
        else:
            self.swap( Index, self.HeapLength )
            self.Heapify( Index )
        self.Heap_Array= self.Heap_Array[ : -1 ]
        self.HeapLength = self.HeapLength - 1
        return          
    
if __name__ == "__main__":
    queries = int( input( ) .strip( ) )
    heap = Heap()
    while queries:
        queries = queries - 1
        query = list( map( int, input().split( ) ) )
        
        if query[0] == 1:
            heap.Add_Element( query[1] )
            continue
    
        elif query[0] == 2:
            heap.Delete_Element( query[1] )
        
        else :
            print( heap.Heap_minimum( ) )