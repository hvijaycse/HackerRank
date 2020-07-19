
def Check( Array):
    Array.sort()
    Temp = []
    length = len(Array)
    for Index in range( length ):
        OR = 0
        for value in Array[ Index: ]:
            OR = OR | value
            if OR in Temp:
                return False
            Temp.append( OR)
    return True

def main():
    TestCase = int( input() )
    while TestCase:
        TestCase -= 1
        N = int( input() )
        Sequence = list( map( int, input().split()))[ : N]

        if Check( Sequence):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
    exit(0)