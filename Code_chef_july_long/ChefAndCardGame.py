def Points( A, B):
    chef, monty = 0, 0
    for i in A:
        chef += int( i)
    for i in B:
        monty += int( i)
    return chef, monty

def main():
    TestCase = int( input())
    while TestCase:
        TestCase -= 1
        N = int( input())
        Chef, Monty = 0, 0 
        while N :
            N -= 1
            Ai, Bi = input().split()
            C, M = Points( Ai, Bi)
            if C > M:
                Chef += 1
            elif M > C:
                Monty += 1
            else:
                Chef += 1
                Monty += 1
        if Chef > Monty:
            print( 0, Chef)
        elif Monty > Chef:
            print( 1, Monty)
        else:
            print(2, Chef)
            
    return

if __name__ == "__main__":
    main()
    exit(0)
