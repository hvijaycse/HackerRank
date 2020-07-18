
# import timeit
'''
This question has a very amazing overlaping subporblem
which must be solved wihtout using DP as in this porblem
DP result in very high memory usage and also the performance
did'nt imporve as i was expecting using DP, it remain almost equal
but in the last 10 minute my mind clicked and saw the overlaping
nature of the porblem and there was not enought time for me to code,
anyways this was really good for me, was able to sit for long hours, and 
i was able to approch problem from a fast approch. Cheers
'''


def main():
    P = int( input()) # This is minimum widht
    Q = int( input()) + 1 # THis is maximum Widht
    R = int( input()) # This is minimum Height
    S = int( input()) + 1 # This is maximum Height
    count = 0
    # start = timeit.default_timer()           
    while P < Q :
        if P != R:
            tmpS = R
            while tmpS < S:
                if tmpS > P:
                    a, b = tmpS, P
                else:
                    a, b = P, tmpS
                while a % b :
                    count = count + a//b
                    b, a = a % b, b
                count = count + a//b
                tmpS = tmpS + 1
            P = P + 1
        else:
            End = min( Q, S)
            while P < End :
                count += 1
                tmpS = P + 1
                thisrow = 0
                while tmpS < End :
                    if tmpS > P:
                        a, b = tmpS, P
                    else:
                        a, b = P, tmpS
                    while a % b :
                        thisrow = thisrow + a//b
                        b, a = a % b, b
                    thisrow = thisrow + a//b
                    tmpS = tmpS + 1
                count += thisrow * 2 
                P += 1
    print( count)
    # stop = timeit.default_timer()
    # print( 'Time:', stop - start)

if __name__ == "__main__":
    main()
    exit(0)