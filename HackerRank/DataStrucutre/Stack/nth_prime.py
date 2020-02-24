def Prime( Number):
    Primes = [2, 3]
    if Number < 3:
        return Primes[: Number]
    Number = Number - 2
    
    while Number:
        isPrime = False
        Num = Primes[-1]
        while not isPrime:
            isPrime = True
            Num = Num + 2
            maxcheck = int( Num ** 0.5) + 1
            for i in Primes:
                if Num % i == 0 :
                    isPrime = False
                    break
                elif i > maxcheck:
                    break
        Primes.append( Num)
        Number = Number - 1       
    return Primes
            
            
    

if __name__ ==  "__main__":
    nth = int( input())
    prime_List = Prime(nth)
    print( prime_List)
    