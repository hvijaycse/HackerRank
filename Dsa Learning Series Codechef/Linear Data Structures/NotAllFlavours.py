

def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        N , K = map( int, input().split() )
        String = list( map( int, input().split()))[ : N ]
        tmp_dict = {}
        for i in range( 1, K + 1):
            tmp_dict[i] = 0
        Maximize = 0
        for i in String:
            tmp_dict[i] = 0
            for k in list(range( 1, i)) + list( range(i + 1, K + 1)):
                tmp_dict[k] += 1
                if tmp_dict[k] > Maximize:
                    Maximize = tmp_dict[k]
        print( Maximize)
            
    return

if __name__ == "__main__":
    main()
    exit(0)