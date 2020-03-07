#!/bin/python3


#
# Complete the downToZero function below.
#
from time import clock

def Downer( array, query):
    if array[query] != float('inf'):
        return
    for i in range( 2, int(query**0.5) + 1):
        if query % i == 0:
            k = query // i
            if array[k] + 1 < array[query]:
                array[query] = array[k] + 1
    if array[query] > array[query - 1] + 1:
        array[query] = array[query - 1] + 1
        
    
def downToZero( Queries, maximum):
    answers = [float('inf')] * (maximum + 1)
    answers[0] = 0
    for i in range( 1, maximum + 1):
        Downer( answers, i)
    for query in Queries:
        print(answers[query])

if __name__ == '__main__':

    q = int(input())
    maximum = -1
    Queries = []

    for q_itr in range(q):
        n = int(input())
        if n > maximum:
            maximum = n
        Queries.append( n)
    Start = clock()
    downToZero(Queries, maximum )
    end = clock()
    print('Time taken ', end - Start)
