from time import time

class Stack():
    
    def __init__(self, Size):
        self.Stack=[0] * Size
        self.Index = -1
        self.Stack_Size = 10

    def pop(self):
        self.Index =self.Index - 1
            
    def Push(self, Element):
        Index = self.Index + 1
        self.Stack[Index] = Element
        self.Index = Index
    
    def Maximum(self):
        return( max( self.Stack[: self.Index + 1] ))
       

if __name__ == "__main__":
    Cases = int( input())
    Stack=Stack(Cases)
    while Cases:
        command =input().split() 
        if command[0] == '1':
            Stack.Push( int(command[1]) )
        elif command[0]  == '2':
            Stack.pop()
        else:
            print('Output ', Stack.Maximum())
        Cases = Cases - 1 
    