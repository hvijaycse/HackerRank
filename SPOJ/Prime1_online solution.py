from math import sqrt
from time import time 
primes = [2]
t0 = time()
for i in range(3,32000,2):
    isprime = True

    cap = sqrt(i)+1

    for j in primes:
        if (j >= cap):
            break
        if (i % j == 0):
            isprime = False
            break
    if (isprime):
        primes.append(i)
        
        

t1 = time()
T = int(input())
output = ""
for t in range(T):

    if (t > 0):
        output += "\n"

    M,N = input().split(' ')
    t2 = time()
    M = int(M)
    N = int(N)
    cap = sqrt(N)+1

    if (M < 2):
        M = 2

    isprime = [True]*100001

    for i in primes:
        if (i >= cap):
            break

        if (i >= M):
            start = i*2
        else:
            start = M + ((i - M % i)%i)

        # The two below, obscure lines create a continuous
        #  block of false elements in order to set all
        #  elements correspnding to numbers divisible by i
        #  in isprime to be false
        # In turns out that this runs substantially faster
        #  than setting the elements individually using loops
        falseblock = [False] * len(isprime[start-M:N+1-M:i]);
        isprime[start-M:N+1-M:i] = falseblock

    for i in range(M,N+1):
        if (isprime[i-M] == True):
            output += str(i) + "\n"

print (output[:-1])
t4 = time()
print('\n time taken to calculate prime is ',(t1 - t0),'\n',
      'Time taken to calcuate and print is ',(t4 - t2))