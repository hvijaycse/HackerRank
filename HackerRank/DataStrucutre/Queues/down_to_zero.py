#!/bin/python3


#
# Complete the downToZero function below.
#
from time import clock


    
def downToZero( Queries, maximum):
    if maximum < 1:
        print(0)
        return
    Array = [float('inf')]*(maximum + 1)
    Array[0] = 0
    Array[1] = 1
    
    for index in range( 2, maximum + 1):
        if Array[index] > Array[index - 1] + 1:
            Array[index] = Array[ index - 1] + 1
        Mul = 2
        while Mul * index < maximum + 1 and Mul <= index:
            if Array[Mul * index] > Array[index] + 1:
                Array[Mul * index] = Array[index] + 1
            Mul = Mul + 1
    for query in Queries:
        print( Array[query])    

if __name__ == '__main__':

    q = int(input())
    maximum = -1
    Queries = []

    for q_itr in range(q):
        n = int(input())
        if n > maximum:
            maximum = n
        Queries.append( n)
    # Start = clock()
    downToZero(Queries, maximum )
    # end = clock()
    # print('Time taken ', end - Start)
