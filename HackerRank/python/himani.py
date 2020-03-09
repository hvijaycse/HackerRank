import math
def solve(arr, n):
    pos_count = 0
    neg_count = 0
    for i in range (n):
        if (arr[i] > 0):
            pos_count += 1
        if (arr[i] < 0):
            neg_count += 1
    result = int(math.pow(2, pos_count))
    if (neg_count > 0):
        result *= int(math.pow(2, neg_count - 1))
    result -= 1
    return result
t = int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    new = []
    for i in arr:
        if i != 0:
            new.append( i)
    n = len(new)
    total = int(math.pow(2,n))-1
    print(total-solve(new,n))
    t-=1