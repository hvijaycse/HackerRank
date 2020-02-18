from time import time

def Prime_list( Start, end):
    if Start == 1:
        Start = 2
    Primes =  list( range( Start, end + 1 ))
    Length = len( Primes)
    Dividers = list( range(2,int(end ** 0.5 ) + 1 ) )
    for Number_index, Number in enumerate(Primes):
        if Number :
            for Divide_index, Divide in enumerate( Dividers):
                if Number % Divide == 0 and Divide < Number:
                    False_Block = [False] * len( Primes [Number_index: : Divide] )
                    Primes [Number_index: : Divide] = False_Block
                    # for i in range( Number_index, Length, Divide):
                    #     Primes[i] = False
                    Dividers.pop( Divide_index)
    return( Primes)

if __name__ == "__main__":
    Times = int( input().strip())
    Output = ''
    for time in range(Times):
        if time > 0:
            Output += '\n'
        
        Start, End = map( int, input().split())
        # t0 = time()
        for number in Prime_list( Start, End):
            if number:
                Output += str( number) + '\n'
    print( Output)
    # t1 = time()
    # print('Time taken = '(t1 - t0))
    exit(0)
    
