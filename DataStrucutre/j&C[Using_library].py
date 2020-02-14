from heapq import heappop,heappush,heapify
from time import clock

file = open( 'J&C[Test_Case_12].txt' )
firstLine = [int(x) for x in file.readline().strip().split()]
cookies = [int(x) for x in file.readline().strip().split()]

cookieCount = int(firstLine[0])
minSweetness = int(firstLine[1])

start=clock()
heapify(cookies)
fC = 0
try:
    while cookies[0] < minSweetness:
        fC+=1
        c1 = heappop(cookies)
        c2 = heappop(cookies)
        newCookie=(1*c1)+(2*c2)
        heappush(cookies,newCookie)
    print(fC)
except:
    print("-1")

end=clock()

print( 'Time Taken ',end-start)