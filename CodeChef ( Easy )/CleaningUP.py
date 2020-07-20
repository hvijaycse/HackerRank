def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))


def main():
    TestCase = Int()
    for _ in range( TestCase):
        Chef = []
        Assitant = []
        C = True
        N, M = map( int, List() )
        Job_done = Ilist()[ : M]
        Jobs = [ True for _ in range( N + 1)]
        
        for Job_index in Job_done:
            Jobs[ Job_index ] = False
    
        for index in range( 1 , N + 1):
            if Jobs[ index]:
                if C:
                    Chef.append(  str(index))
                    C = False
                else:
                    Assitant.append( str(index))
                    C = True
        
        print( ' '.join( Chef))
        print( ' '.join( Assitant))
if __name__ == "__main__":
    main()
    exit(0)