

def main():
    N = int( input())
    Choc = list( map( int, input().split()))
    Choc.sort()
    Mul = 1
    summer = 0
    for i in range( N -1 , -1, -1):
        summer += Choc[i]*Mul
        Mul += 1
    print( summer)

if __name__ == "__main__":
    main()
    exit(0)