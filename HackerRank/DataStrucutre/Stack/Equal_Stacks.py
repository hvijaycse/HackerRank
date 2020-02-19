#!/bin/python3

#
# Complete the equalStacks function below.
#

class Stack_Height():
    
    def __init__(self, Array):
        self.Height = 0
        self.Stack = list( reversed( Array))
        self.Head = len(Array) -1
        for element in Array:
            self.Height = self.Height + element
    
    def POP(self ):
        self.Height = self.Height - self.Stack[self.Head]
        self.Head = self.Head - 1
        return self.Height

def equalStacks( h1, h2, h3):
    Min_Height = float('+inf')
    Stack1 = Stack_Height(h1)
    if Stack1.Height < Min_Height:
        Min_Height = Stack1.Height
    
    Stack2 = Stack_Height(h2)
    if Stack2.Height < Min_Height:
        Min_Height = Stack2.Height
    
    Stack3 = Stack_Height(h3)
    if Stack3.Height < Min_Height:
        Min_Height = Stack3.Height
    
    Stacks =  [Stack1, Stack2, Stack3]
    while Stacks[0].Height != Stacks[1].Height or Stacks[1].Height != Stacks[2].Height or Stacks[1].Height != Min_Height:
        for Stack in Stacks:
            while Stack.Height > Min_Height:
                current = Stack.POP()
                if current < Min_Height:
                    Min_Height = current
    return Min_Height
                        
if __name__ == '__main__':
    
    file = open('stack.txt')
    n1N2N3 = file.readline().strip().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, file.readline().strip().split()))

    h2 = list(map(int, file.readline().strip().split()))

    h3 = list(map(int, file.readline().strip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)
    exit(0)
