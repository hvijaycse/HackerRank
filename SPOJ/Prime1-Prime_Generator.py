from time import time

def SieveOfEratosthenes( Number ):
    # Prime_List = [ True for i in range( Number + 1)]
    Prime_List = [ True] * ( Number + 1)
    Start = 2
    while( Start * Start <= Number):
        if Prime_List[ Start] :
            for i in range( Start << 1, Number + 1, Start):
                Prime_List[i] = False
        Start = Start + 1
    Prime_List[1] = False
    return Prime_List
            

if __name__ == "__main__":
    Times = int( input().strip())
    Biggest = 0
    Cases = []
    while Times:
        Start, End = map( int, input().split())
        if End > Biggest:
            Biggest = End
        Cases.append( ( Start, End) )
        Times = Times - 1
    t0 = time()
    print( SieveOfEratosthenes( Biggest)) 
    # for Case in  Cases:
    #     for i in range( Case[0], Case[1] + 1):
    #         if Prime_List[i]:
    #             print( i )
    #     print(' ')
    t1 = time()
    
    print('Time taken is ', t1 - t0)
    
    exit(0)
    
