#!/bin/python3

import os
import sys

# Complete the solve function below.

def solved( Array, D):
    Length = len( Array)
    Maximum = float('-inf')
    for Index in range(0, D):
        if Array[Index] > Maximum:
            Maximum = Array[Index]
    Minimum = Maximum
    Index = Index + 1
    while Index < Length:
        Removed = Array[Index - D]
        Added = Array[Index]
        if Removed == Maximum:
            Maximum = float('-inf')
            for i in range( Index - D + 1, Index):
                if Array[i] > Maximum:
                    Maximum = Array[i]
        if Added > Maximum :
            Maximum = Added
        if Minimum > Maximum:
            Minimum = Maximum
        Index += 1
    
    return Minimum

def solve(arr, queries):
    Ans = []
    for query in queries:
        Ans.append( solved( arr, query))
    return Ans

if __name__ == '__main__':
    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    arr = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)
    result = solve(arr, queries)
    print( '\n'.join( map( str, result) ) )