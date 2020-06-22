def main():
    N = int( input() )
    Budget = []
    for i in range(N ):
        Budget.append( int ( input()))
    Budget.sort()
    Maximum = 0
    Length = len( Budget)
    for i in range( Length):
        current = Budget[i] * ( Length - i)
        if current > Maximum:
            Maximum = current
    print( Maximum)
    return

if __name__ == "__main__":
    main()
    exit(0)