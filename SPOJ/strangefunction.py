#!/bin/python3

import math
import os
import time


# Complete the maximumValue function below.

def maximumValue(n,array):
    max_val=float('-inf')

    while n:
        i=n
        while i:
            key=array[i-1]
            if i==n:
                current_max=key
                current_gcd=key
                current_sum=key
                value=0
            elif current_gcd==1:
                if current_max<key:
                    current_max=key
                current_sum+=key
                if current_sum<=0:
                    i=i-1
                    continue
                value=current_sum-current_max
                if value>max_val:
                    max_val=value

            else:
                if current_max<key:
                    current_max=key
                current_sum+=key
                current_gcd=math.gcd(current_gcd,key)
                if current_sum<=0:
                    i=i-1
                    continue
                value=current_gcd*(current_sum-current_max)
                if value>max_val:
                    max_val=value
            i=i-1
        print((i,n),current_gcd,current_sum,current_max,max_val,'\n')
        n=n-1
    return max_val

        


if __name__ == '__main__':
    file=open('data.txt')
    n = int(file.readline().strip())
    a = list(map(int, file.readline().strip().split()))
    print("\n\n\t Strting to solve the problem")
    input()
    start=time.clock()
    result = maximumValue(50000,a[:50000])
    end=time.clock()
    print(result)

    print("time consumed is ",end-start)
    input()