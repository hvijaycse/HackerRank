import math 
import time
import random

def max_arr(a):
    maxi=a[0]
    for value in a:
        if maxi<value:
            maxi=value
    return maxi


count=0
for i in range(1000):
    array=[random.randint(10,5000) for i in range(1000)]
    a=time.clock()
    print(max(array))
    b=time.clock()
    print(max_arr(array))
    c=time.clock()
    if b-a >c-b :
        count+=1
print('\n')
print(' the no of time you were faster than max functio in 1000 times ',count)
