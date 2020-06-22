
def Rev( String):
    length = len( String)
    for i in range( length //2 ):
        a = String[i]
        b = String[ length - i - 1]
        String[i] = b
        String[ length - i - 1] = a
    return ''.join(String)

def main():
    N = int( input())
    LS = []
    while N:
        N = N - 1
        num = input()
        num = [i for i in num]
        LS.append(num)
    for num in LS:
        num = Rev( num)
        print( int( num) )
    return

if __name__ == "__main__":
    main()
    exit(0)