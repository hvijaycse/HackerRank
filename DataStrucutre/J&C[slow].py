import os
import sys


class Min_heap():
    
    def Parent(self, Index ):
        return Index // 2
    
    def Left ( self, Index):
        return Index * 2
    
    def Right ( self, Index):
        return (Index * 2) +1
    
    def __init__(self ):
        self.Heap_Length = 0
        self.Heap_Array = [ float('-inf') ]
    
    def Swap (self, Index_1, Index_2 ):
        temp = self.Heap_Array[ Index_1 ]
        self.Heap_Array[ Index_1] = self.Heap_Array[ Index_2 ]
        self.Heap_Array[ Index_2] = temp 
        return
    
    def Heapify( self, Index):
        Left = self.Left( Index )
        Right = self.Right( Index )
        minimum=Index
        
        if Right <= self.Heap_Length and self.Heap_Array[ Right ] < self.Heap_Array[ minimum]:
            minimum=Right
        if Left <= self.Heap_Length and self.Heap_Array[ Left ] < self.Heap_Array[ minimum]:
            minimum=Left
        
        if minimum != Index:
            self.Swap( Index, minimum)
            self.Heapify( minimum )
        return
    
    def Update_Key( self, Index, value):
        if self.Heap_Array[ Index ] < value:
            print( ' Key already minimum ')
        else:
            self.Heap_Array[ Index ] = value
            while Index >=1 and self.Heap_Array[ self.Parent( Index ) ]  > self.Heap_Array[ Index ] :
                self.Swap( Index, self.Parent( Index ))
                Index=self.Parent( Index )
                
        
    def Create_heap(self, Array):
        self.Heap_Array = self.Heap_Array + Array
        self.Heap_Length = self.Heap_Length + len( Array )
        Index = self.Heap_Length // 2
        
        while Index:
            self.Heapify( Index )
            Index = Index - 1
        return
    
    def Delete(self, Index):
        if self.Heap_Array[ self.Heap_Length ] < self.Heap_Array[ Index]:
            self.Update_Key( Index, self.Heap_Array[ self.Heap_Length ] )
            self.Heap_Array=self.Heap_Array[: -1]
            self.Heap_Length = self.Heap_Length - 1   
        else:
            self.Swap( Index, self.Heap_Length )
            self.Heap_Array=self.Heap_Array[: -1]
            self.Heap_Length = self.Heap_Length - 1     
            self.Heapify( Index )
        return
        
    def Minimim( self):
        return self.Heap_Array[1]
    
    
    def Pop_Min( self ):
        if self.Heap_Length == 0:
            value = -1
        else:
            value=self.Minimim()
            self.Delete( 1 )
        return value 
            
    def Add_Element(self, Element):
        self.Heap_Array.append( float('+inf' ) )
        self.Heap_Length = self.Heap_Length + 1
        self.Update_Key( self.Heap_Length, Element ) 
        return
        

        
         
def cookies(k, A):
    Cookie_Heap = Min_heap()
    Cookie_Heap.Create_heap( A )
    operations = 0
    sweetness=Cookie_Heap.Minimim()
    while sweetness < k :
        First=Cookie_Heap.Pop_Min()
        Second=Cookie_Heap.Pop_Min()
        if First == -1 or Second == -1:
            return -1
        Cookie_Heap.Add_Element( First + ( Second * 2) )
        sweetness=Cookie_Heap.Minimim()
        operations = operations + 1
    
    return operations
        
    
    

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)
    print( result )