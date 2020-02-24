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


if __name__ == '__main__':
    Plate, Qprimes = map( int, input().split() )
    Plates = list( map(int, input().split() ))
    PrimeList = Prime(Qprimes)
    BS = []
    i = 0
    while i < Qprimes:
        Prime_num = PrimeList[ i]
        New_Paltes = []
        New_B = []
        while Plates:
            element = Plates.pop()
            if element % Prime_num == 0:
                New_B.append(element)
            else:
                New_Paltes.append( element)
        New_B.reverse()
        BS.append(New_B)
        Plates = New_Paltes
        i = i+1
    Plates.reverse()
    
    for b in BS:
        for element in b:
            print(element)
    for plate_remaining in Plates:
        print(plate_remaining)
    exit(0)
    
    