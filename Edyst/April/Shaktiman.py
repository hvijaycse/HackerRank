def Int():
    return int( input() )

def List():
    return input().split()

def Ilist():
    return list( map( int, input().split()))

def yes():
    print('YES')

def no():
    print('NO')

def main():
    TestCase = Int()
    for _ in range(TestCase):
        N, P = Ilist()
        max_capcity = N * (N + 1) // 2
        if P == max_capcity:
            Array = [i for i in range( 1, N + 1)]
        elif P > max_capcity:
            Array = [ i for i in range( 1, N + 1)]
            Array[0] += P - max_capcity
        else:
            Array = [1 for i in range( N)]
            Index = 0
            while P > N:
                Array[ Index] = Index + 1
                P = P - N
                N -= 1 
                Index += 1
            for i in range( Index, Index + P):
                Array[i] = Index + 1
            for i in range( Index + P, len( Array)):
                Array[i] = Index
        for value in Array:
            print( value, end = ' ')
        print()

if __name__ == "__main__":
    main()
    exit(0)