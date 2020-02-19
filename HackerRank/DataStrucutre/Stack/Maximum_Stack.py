
class Stack():
    
    def __init__(self, Size):
        self.Stack=[0] * Size
        self.Head = -1
        
        self.Max_Stack=[0] *(Size + 1)
        self.Max_Head = 1

    def pop(self):
        if self.Stack[self.Head] == self.Max_Stack[self.Max_Head - 1] :
            self.Max_Stack[self.Max_Head - 1] = 0
            self.Max_Head = self.Max_Head - 1
        self.Head = self.Head - 1
            
    def Push(self, Element):
        Head = self.Head + 1
        Max_Head = self.Max_Head 
        self.Stack[Head] = Element
        if Element >= self.Max_Stack[ Max_Head - 1]:
            self.Max_Stack[Max_Head] = Element
            self.Max_Head = Max_Head + 1
        self.Head = Head
    
    def Maximum(self):
        return self.Max_Stack[self.Max_Head -1 ]
       

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
            print( Stack.Maximum() )
        Cases = Cases - 1 
    
    