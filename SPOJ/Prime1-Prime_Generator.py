
if __name__ == "__main__":
    primes = [2]
    for number in range(3, 32000,2):
        Max_Check = int(number ** 0.5)
        Isprime = True
        for prime in primes:
            if number > Max_Check:
                break
            if number% prime == 0:
                Isprime = False
                break
        if Isprime :
            primes.append(number)
    Tests = int( input())
    output = ""
    for test in range(Tests):
        Start, End = list( map( int, input().split()))
        if Start < 2:
            Start = 2
        Max_Check = int( End ** 0.5) + 1
        TrueList = [True] * 100001
        for i in primes:
            if (i >= Max_Check):
                break

            if (i >= Start):
                start = i*2
            else:
                start = Start + ((i - Start % i)%i)
                
            falseblock = [False] * len(TrueList[start-Start:End+1-Start:i]);
            TrueList[start-Start:End+1-Start:i] = falseblock
        for i in range(Start, End + 1):
            if (TrueList[i-Start] == True):
                output += str(i) + "\n"
    
    print( output[:-1])
        
        