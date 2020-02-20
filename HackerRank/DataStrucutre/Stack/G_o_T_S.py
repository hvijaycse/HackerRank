#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
class Stacking():
    
    def __init__(self, Array):
        self.Stack = Array
        self.Head = 0
        self.Length = len(Array)
    
    def pop(self ):
        self.Head = self.Head + 1
        return self.Stack[self.Head - 1]   
    
    def Last(self ):
        return self.Stack[self.Head]
    def Check(self ):
        return self.Length - self.Head
    
def twoStacks(x, a, b):
    Stack1 = Stacking(a)
    Stack2 = Stacking(b)
    Summision = 0
    steps = 0    
    while Summision < x -1 :
        steps += 1
        if Stack1.Stack:
            Minimum = Stack1
        else:
            Minimum = Stack2
        if  Stack2.Stack :
            if Stack2.Last() < Minimum.Last():
                Minimum = Stack2
        Summision += Minimum.pop()
    return steps

if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)
        print(result)


