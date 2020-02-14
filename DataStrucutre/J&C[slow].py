import os
import sys
import time

class Min_heap():
    
    def Parent(self, Index ):
        return Index >> 1
    
    def Left ( self, Index):
        return Index << 1
    
    def Right ( self, Index):
        return (Index << 1 ) +1
    
    def __init__(self ):
        self.Heap_Length = 0
        self.Heap_Array = [ float('-inf') ]
    
    def Swap (self, Index_1, Index_2 ):
        self.Heap_Array[ Index_1 ] =  self.Heap_Array[ Index_1 ] ^ self.Heap_Array[ Index_2 ]
        self.Heap_Array[ Index_2] = self.Heap_Array[ Index_2 ] ^ self.Heap_Array[ Index_1 ]
        self.Heap_Array[ Index_1 ] =  self.Heap_Array[ Index_1 ] ^ self.Heap_Array[ Index_2 ]
        return
    
    def Minimim(self ):
        return self.Heap_Array[ 1 ] 
    
    def Heapify( self, Index):
        minimum=Index
        left = self.Left( Index )
        right = self.Right( Index )
        lenght = self.Heap_Length
        if  left <= lenght and  self.Heap_Array[ Index ] > self.Heap_Array[ left ]:
            minimum=left
        if  right <= lenght and self.Heap_Array[ minimum ] > self.Heap_Array[ right ]:
            minimum=right
        if minimum != Index:
            self.Swap( Index, minimum)
            self.Heapify( minimum )
        return
        
    def Create_heap(self, Array):
        self.Heap_Array = self.Heap_Array + Array
        self.Heap_Length = len( Array )
        Index = self.Heap_Length >> 1
        
        while Index:
            self.Heapify( Index )
            Index = Index - 1
        return
    
    def Add_Element(self, Element):
        self.Heap_Array.append( Element )
        self.Heap_Length = self.Heap_Length + 1
        Index = self.Heap_Length
        while Index >= 1 and self.Heap_Array[ Index ] < self.Heap_Array[ self.Parent( Index )]:
            self.Swap( Index, self.Parent( Index ) )
            Index = self.Parent( Index )
        return
    
    def Extract_Min( self ):
        if self.Heap_Length < 1:
            Minimum = -1 
        else:
            Minimum = self.Heap_Array[ 1 ]
            self.Swap( 1, self.Heap_Length)
            self.Heap_Length = self.Heap_Length - 1
            self.Heap_Array = self.Heap_Array[ :-1]
            self.Heapify( 1 )
        return Minimum
            
def cookies(k, A):
    if A.count( 0 ) >=2:
        return -1
    Cookie_Heap = Min_heap()
    Cookie_Heap.Create_heap( A )
    operations = 0
    sweetness=Cookie_Heap.Minimim()
    while sweetness < k :
        First = Cookie_Heap.Extract_Min( )
        Second = Cookie_Heap.Extract_Min( )
        if First == -1 or Second == -1:
            return -1
        Cookie_Heap.Add_Element( First + ( Second << 1) )
        sweetness=Cookie_Heap.Minimim()
        operations = operations + 1
    
    return operations
        
    
    

if __name__ == '__main__':
    file = open( 'J&C[Test_Case_12].txt' )
    nk = file.readline().strip().split()
    n = int(nk[0])
    k = int(nk[1])
    A = list(map(int, file.readline().rstrip().split()))
    start = time.clock()
    result = cookies(k, A)
    end=time.clock()
    print( result , 'Time Taken =', (end - start) )